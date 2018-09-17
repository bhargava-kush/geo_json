from django.contrib.gis.geos import Point
from django.contrib.gis.geos import fromstr
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Providers,Polygons
from .serializers import ProvidersSerializer,PolygonsSerializer
# Create your views here.

class ProvidersViewSet(viewsets.ModelViewSet):
    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer

class PolygonsViewSet(viewsets.ModelViewSet):
    serializer_class = PolygonsSerializer
    queryset = Polygons.objects.all()

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors)


    def get_queryset(self):
        queryset = Polygons.objects.all()
        area = self.request.query_params.get('area',None)
        if area is not None:
            # area = [3.4345674,8.986549]
            area_point = eval(self.request.query_params.get('area'))
            coordinates = [float(x) for x in area_point]
            point_wkt = Point(coordinates[0],coordinates[1]).wkt
            pnt = fromstr(point_wkt)
            queryset = queryset.filter(coordinates__contains=pnt)
        return queryset


