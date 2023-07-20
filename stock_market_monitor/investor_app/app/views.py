from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Asset
from django.urls import reverse
from .forms import AssetForm, EditAssetForm
import yfinance as yf


# Create your views here.

def assets(request):
    assets_list = Asset.objects.all()
    paginator = Paginator(assets_list, 5)
    page = request.GET.get('page')
    
    assets = paginator.get_page(page)

    return render(request, 'assets-list.html', {'assets': assets})


def get_asset_price(asset_name):
    try:
        ticker = yf.Ticker(asset_name + '.SA')
        data = ticker.history(period='1d')
        asset_price = round(data['Close'].iloc[-1], 2)
        return asset_price
    except Exception as e:
        return None


def new_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset_name = request.POST['name'].upper()
            asset_price = get_asset_price(asset_name)
            if asset_price is not None:
                asset.value = asset_price
                asset.save()
                return redirect(reverse('assets'))
            else:
                messages.error(
                    request, 'Erro ao obter o preço do ativo. Verifique o nome do ativo.')
    else:
        form = AssetForm()
    return render(request, 'add-asset.html', {'form': form})


def edit_asset(request, id):
    asset = get_object_or_404(Asset, pk=id)
    form = EditAssetForm(instance=asset)

    if request.method == 'POST':
        form = EditAssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect(reverse('assets'))
        else:
            return render(request, 'edit-asset.html', {'form': form, 'asset': asset})
    else:
        return render(request, 'edit-asset.html', {'form': form, 'asset': asset})


def delete_asset(request, id):
    asset = get_object_or_404(Asset, pk=id)
    asset.delete()

    messages.info(request, 'Ação deletada com sucesso.')
    return redirect(reverse('assets'))
