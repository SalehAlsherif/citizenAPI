from rest_framework import serializers
from .models import Citizen

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = ['national_id', 'birth_date', 'birth_place']
        read_only_fields = ['birth_date', 'birth_place']
         
        
    
    