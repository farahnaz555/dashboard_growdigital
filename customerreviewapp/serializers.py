from rest_framework import serializers
from .models import customerreviewpage

class CustomerReviewSerializer(serializers.ModelSerializer):

	class Meta:
		model = customerreviewpage
		fields = '__all__'