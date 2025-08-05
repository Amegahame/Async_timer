from django.urls import path
from .views import async_timer_view

urlpatterns = [
    path('async-timer/', async_timer_view, name='async_timer'),
]
