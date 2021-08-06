from rest_framework import serializers
from .models import careerpagepage

class CareerPageSerializer(serializers.ModelSerializer):

	class Meta:
		model = careerpagepage
		fields = '__all__'