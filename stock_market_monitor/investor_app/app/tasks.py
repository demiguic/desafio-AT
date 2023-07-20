from .models import Asset
import yfinance as yf
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def update_assets(asset_id):
    try:
        asset = Asset.objects.get(id=asset_id)
        ticker = yf.Ticker(asset.name + '.SA')
        data = ticker.history(period='1d')
        asset_price = round(data['Close'].iloc[-1], 2)
        asset.value = asset_price

        suggestion = None
        if asset_price > asset.superior_limit:
            suggestion = 'Vender'
        elif asset_price < asset.inferior_limit:
            suggestion = 'Comprar'

        if suggestion and not asset.email_sent_status:
            envia_email(asset, suggestion)
            asset.email_sent_status = True
        elif not suggestion:
            asset.email_sent_status = False

        asset.save()
        logger.info(f'Atualizei {asset.name}')
    except Asset.DoesNotExist:
        logger.error(f'Asset com ID {asset_id} não encontrado.')
    except Exception as e:
        logger.error(
            f'Ocorreu um erro durante a atualização do asset: {str(e)}')


def envia_email(asset, suggestion):
    title = f'Sugestão de Atividade: {suggestion} {asset.name}'
    body = f'Olá, a ação {asset.name} está com o valor de R$ {asset.value} e está na hora de {suggestion.lower()}!'

    send_mail(
        title,
        body,
        'settings.EMAIL_HOST_USER',
        ["agdcj.eng20@uea.edu.br"],
        fail_silently=False)
    logger.info("Email enviado")
