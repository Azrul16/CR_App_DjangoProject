from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['Course_Code','Course_Title', 'Course_Teacher', 'date', 'time']