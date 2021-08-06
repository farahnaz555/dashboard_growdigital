from rest_framework import serializers
from .models import homepage, aboutuspage, termsncpage, privacypolicypage, sitemappage

class HomeSerializer(serializers.ModelSerializer):

	class Meta:
		model = homepage
		fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):

	class Meta:
		model = aboutuspage
		fields = '__all__'


class TermsSerializer(serializers.ModelSerializer):

	class Meta:
		model = termsncpage
		fields = '__all__'


class PrivacyPolicySerializer(serializers.ModelSerializer):

	class Meta:
		model = privacypolicypage
		fields = '__all__'


class SiteMapSerializer(serializers.ModelSerializer):

	class Meta:
		model = sitemappage
		fields = '__all__'


