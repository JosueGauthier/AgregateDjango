from django.urls import path, include
from .models import *
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class BookSerializer(serializers.HyperlinkedModelSerializer):
    total_amount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Book
        fields = ['name', 'pages','total_amount']

    def get_total_amount(self, obj):
        return obj.get_total()

# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



""" class BookStatSerializer(serializers.HyperlinkedModelSerializer):
    total_amount = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Book
        fields = ['total_amount']

    def get_total_amount(self, obj):
        return obj.get_total() """

class BookStatSerializer(serializers.Serializer):
    total_amount = serializers.SerializerMethodField(read_only=True)

    def get_total_amount(self):
        return Book.get_total()


from rest_framework.response import Response


""" class BookStatViewSet(viewsets.ViewSet):
    queryset = Book.objects.all()
    serializer_class = BookStatSerializer 

    def list(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        serializer = BookStatSerializer
        return Response(serializer.data) """
        





""" class BookStatViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookStatSerializer """


import json
from django.http import JsonResponse


def api_total(request, *args, **kwargs):
    model_data = Book.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['pages'] = model_data.pages
        
    return JsonResponse(data)


from django.db.models import Avg
def get_total(request, *args, **kwargs):
    #model_data = Book.objects.all().order_by("?").first()
    #data = {}

    data = []
    data.append(Book.objects.all().aggregate(Avg('price')))
    
    #data['total-amount'] = Book.objects.all().aggregate(Avg('price'))
    #data['pages'] = model_data.pages
        
    return JsonResponse(data, safe=False)



router = routers.DefaultRouter()
router.register(r'book', BookViewSet)
#router.register(r'stat', BookStatViewSet)

urlpatterns = [
    path('total/', get_total), # localhost:8000/api/
    #path('', views.product_list_create_view),
    #path('api/', BookViewSet.as_view())
    path('', include(router.urls)),
]