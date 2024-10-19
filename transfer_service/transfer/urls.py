from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransferViewSet

router = DefaultRouter()
router.register(r'transfer', TransferViewSet)

urlpatterns = [
    path('', include(router.urls)),
]