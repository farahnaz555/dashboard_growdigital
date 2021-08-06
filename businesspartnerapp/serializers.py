from rest_framework import serializers
from .models import businesspartnerpage

class BusinessPartnerSerializer(serializers.ModelSerializer):

	class Meta:
		model = businesspartnerpage
		fields = '__all__'