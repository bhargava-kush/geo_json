from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Providers,Polygons
from .serializers import ProvidersSerializer,PolygonsSerializer
# Create your views here.

class ProvidersViewSet(viewsets.ViewSet):
    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer

    def list(self,request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrive(self,request,pk=None):
        provider = get_object_or_404(self.queryset, pk=pk)
        serializer = ProvidersSerializer(provider)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors)

    def destroy(self,request,pk=None):
        provider = get_object_or_404(self.queryset, pk=pk)
        provider.delete()
        return Response("Provider Deleted")

    def update(self,request,pk=None):
        provider = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.update(request.data,provider)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PolygonsViewSet(viewsets.ViewSet):
    serializer_class = PolygonsSerializer
    queryset = Polygons.objects.all()

    def self_queryset(self):
        area_point = self.request.query_params.get('area')
        # area = [[3.44,8.99],[4.22,5.32],[3.4,5.777]]
        for point in area_point:
            a = 'POLYGON'

        # coordinates = [i for i in area]
