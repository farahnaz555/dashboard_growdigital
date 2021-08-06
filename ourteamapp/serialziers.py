from rest_framework import serializers
from .models import ourteampage

class OurTeamSerializer(serializers.ModelSerializer):

	class Meta:
		model = ourteampage
		fields = '__all__'