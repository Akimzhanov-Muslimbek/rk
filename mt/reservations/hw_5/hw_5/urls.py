from django.contrib import admin
from django.urls import path, include  # добавляем include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),  # Подключаем маршруты приложения clients
]
