from rest_framework import viewsets
from .models import Data
from .serializers import DataSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()

    def get_serializer_class(self):
        return DataSerializer
