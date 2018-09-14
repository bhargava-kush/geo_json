from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Providers,Polygons



class ProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Providers
        fields = '__all__'

    def create(self, validated_data):
        provider = Providers.objects.create(name=validated_data['name'],email=validated_data['email'],phone_number=validated_data['phone_number'], language=validated_data['language'],
                                                    currency=validated_data['currency'])

    def update(self,validated_data,provider):
        provider.name = validated_data['name']
        provider.email = validated_data['email']
        provider.phone_number = validated_data['phone_number']
        provider.language = validated_data['language']
        provider.currency = validated_data['currency']
        provider.save()
        return provider

class PolygonsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Polygons
        geo_field = "coordinates"
        fields = ('name','price',)
