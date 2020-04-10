from django.urls import path

from products.views import ProductListView, ProductDetailSlugView, home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('product/', ProductListView.as_view(), name='list'),
    path('product/<slug>/', ProductDetailSlugView.as_view(), name='detail'),
]
