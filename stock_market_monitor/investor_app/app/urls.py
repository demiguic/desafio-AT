from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.assets, name='assets'),
    path('newasset/', views.newAsset, name='new-asset'),
    path('edit/<int:id>', views.editAsset, name='edit-asset'),
    path('delete/<int:id>', views.deleteAsset, name='delete-asset'),
]