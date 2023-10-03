from django.urls import path
from catalog.views import ProductListView, ContactsListView, ProductDetailView

app_name = 'catalog'
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('product/<pk>', ProductDetailView.as_view(), name='contacts'),
]
