from django.urls import path, re_path, include
from django.contrib import admin
import debug_toolbar
from rest_framework.authtoken.views import obtain_auth_token
from .views import home  # <-- importe a view

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', home),  # <-- rota raiz
    re_path('bookstore/(?P<version>(v1|v2))/', include('order.urls')),
    re_path('bookstore/(?P<version>(v1|v2))/', include('product.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
