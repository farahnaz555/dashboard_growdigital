from rest_framework import serializers
from .models import priceandpackagesmodel

class PriceAndPackageSerializer(serializers.ModelSerializer):

	class Meta:
		model = priceandpackagesmodel
		fields = '__all__'

