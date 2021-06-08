from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', include('authentication.api.urls')),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/tg_bot/', include('tg_bot.api.urls')),
]
