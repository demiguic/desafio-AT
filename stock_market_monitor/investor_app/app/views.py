from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Asset
from .forms import AssetForm, EditAssetForm
import yfinance as yf


# Create your views here.


def login(request):
    return render(request, 'login.html')


def assets(request):
    assets = Asset.objects.all()

    return render(request, 'assets-list.html', {'assets': assets})


def newAsset(request):

    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset_name = request.POST['name'].upper()
            ticker = yf.Ticker(asset_name + '.SA')
            data = ticker.history(period='1d')
            asset_price = round(data['Close'].iloc[-1], 2)
            print(asset_price)
            asset.value = asset_price

            asset.save()
            return redirect('/')

    else:
        form = AssetForm()
        return render(request, 'add-asset.html', {'form': form})


def editAsset(request, id):
    asset = get_object_or_404(Asset, pk=id)
    form = EditAssetForm(instance=asset)

    if (request.method == 'POST'):
        form = AssetForm(request.POST, instance=asset)
        if (form.is_valid()):
            asset.save()
            return redirect('/')
        else:
            return render(request, 'edit-asset.html', {'form': form, 'asset': asset})

    else:
        return render(request, 'edit-asset.html', {'form': form, 'asset': asset})


def deleteAsset(request, id):
    asset = get_object_or_404(Asset, pk=id)
    asset.delete()

    messages.info(request, 'Ação deletada com sucesso.')

    return redirect('/')
