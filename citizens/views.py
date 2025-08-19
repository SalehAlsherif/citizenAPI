from django.shortcuts import render
from rest_framework import viewsets
from .models import Citizen
from .serializers import CitizenSerializer
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
class CitizenViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
    # Create your views here.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:

            citizen.full_clean()  # Triggers model validation
            citizen.save()
            return Response(self.get_serializer(citizen).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'error': e.message_dict}, status=status.HTTP_400_BAD_REQUEST)