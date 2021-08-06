from rest_framework import serializers
from .models import consultationpage

class ConsultationPageSerializer(serializers.ModelSerializer):

	class Meta:
		model = consultationpage
		fields = '__all__'