from rest_framework import serializers
from .models import portfoliopage

class PortfolioSerializer(serializers.ModelSerializer):

	class Meta:
		model = portfoliopage
		fields = '__all__'

