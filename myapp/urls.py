from django.urls import path,include
from rest_framework import routers
from .views import DataViewSet

router = routers.DefaultRouter()
router.register('data', DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]