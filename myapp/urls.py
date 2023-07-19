from django.urls import path
from .views import Another

urlpatterns = [
    path('', Another.as_view()),
]