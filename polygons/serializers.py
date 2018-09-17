from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Providers,Polygons



class ProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Providers
        fields = '__all__'


class PolygonsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Polygons
        geo_field = "coordinates"
        fields = ('name','price',)

    def create(self, validated_data):
        provider_obj = Providers.objects.get(pk=validated_data['provider_id'])
        polygons = Polygons.objects.create(providers=provider_obj,name=validated_data['name'],price=validated_data['price'],coordinates=validated_data['coordinates'])

