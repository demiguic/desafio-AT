from background_task import background
from .models import Asset
import yfinance as yf
from django.core.mail import send_mail
from django.conf import settings


@background(schedule=5)
def update_assets():
    assets = Asset.objects.all()
    for asset in assets:
        ticker = yf.Ticker(asset.name + '.SA')
        data = ticker.history(period='1d')
        asset_price = round(data['Close'].iloc[-1], 2)
        asset.value = asset_price
        if asset_price > asset.superior_limit:
            if not asset.email_sent_status:
                envia_email(asset.id, 'Vender')
                asset.email_sent_status = True
        elif asset_price < asset.inferior_limit:
            if not asset.email_sent_status:
                envia_email(asset.id, 'Comprar')
                asset.email_sent_status = True
        else:
            asset.email_sent_status = False
        asset.save()
        print(f'atualizei {asset.name}')

# Agende a primeira execução manualmente após cadastrar uma nova ação
# E a partir daí, as próximas execuções serão agendadas automaticamente com o intervalo específico da ação.
for asset in Asset.objects.all():
    update_assets(repeat=1, repeat_until=None)


def envia_email(asset_id, suggestion):
    asset = Asset.objects.get(id=asset_id)
    title = f'{suggestion} "{asset.name}'
    body = f'Olá, a ação {asset.name} está com o valor de R$ {asset.value} e está na hora de {suggestion}!'

    send_mail(
        title,
        body,
        'settings.EMAIL_HOST_USER',
        ["agdcj.eng20@uea.edu.br"],
        fail_silently=False)
    print("enviei")
