from django import forms


from .models import Asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('name', 'superior_limit', 'inferior_limit', 'interval')

class EditAssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('name', 'superior_limit', 'inferior_limit', 'interval')