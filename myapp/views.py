from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Data

# Create your views here.
class Another(View):
    datas = Data.objects.all()

    def get(self, request):
        return HttpResponse('This is from Another view')