from django.urls import path
from .views import ChangeDetection

urlpatterns = [
    path('change-detection/', ChangeDetection.as_view(), name='change-detection'),
]