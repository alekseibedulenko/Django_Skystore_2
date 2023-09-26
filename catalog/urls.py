from django.urls import path
from catalog.views import home, contacts, detail_product

app_name = 'catalog'
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<pk>', detail_product, name='contacts'),
]
