from rest_framework import serializers
from .models import servicespage

class ServicesSerializer(serializers.ModelSerializer):

	class Meta:
		model = servicespage
		fields = '__all__'

