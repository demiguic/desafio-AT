from django.urls import path
from . import views

urlpatterns = [
    path('', views.assets, name='assets'),
    path('newasset/', views.new_asset, name='new-asset'),
    path('edit/<int:id>', views.edit_asset, name='edit-asset'),
    path('delete/<int:id>', views.delete_asset, name='delete-asset'),
]