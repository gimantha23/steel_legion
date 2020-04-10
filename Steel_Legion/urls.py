from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from .views import (
    login_page,
    register_page,
    logout_request
)

from carts.views import checkout_page, order_confirmed_page

app_name = 'carts'
urlpatterns = [

    path('login/', login_page, name='login'),
    path('logout/', logout_request, name='logout'),
    path('register/', register_page, name='register'),
    path('checkout/', checkout_page, name='checkout'),
    path('checkout/order', order_confirmed_page, name='order'),
    path('admin/', admin.site.urls),
    path('', include("products.urls")),
    path('search/', include("search.urls")),
    path('cart/', include("carts.urls")),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
