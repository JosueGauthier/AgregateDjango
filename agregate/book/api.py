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
    model_data = Book.objects.all().order_by("?").first()
    data = {}
    
    data['total-amount'] = Book.objects.all().aggregate(Avg('price'))
    #data['pages'] = model_data.pages
        
    return JsonResponse(data)

""" 
def get_total_salary(self, obj):
        user = self.context['request'].user.staffs.full_name
        totalsalary = VaPayroll.objects.filter(Q(status='APPROVED-BY-THE-MANAGER'),
            Q(virtual_assistant=user),
            Q(date__month=datetime.date.today().month),
        Q(date__year=datetime.date.today().year)).aggregate(total_salary=Sum('salary'))

        return totalsalary['total_salary']
        
 """
# Routers provide an easy way of automatically determining the URL conf.
""" router = routers.DefaultRouter()
router.register(r'book', BookViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-book/', include('rest_framework.urls', namespace='rest_framework'))
]
"""

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)


urlpatterns = [
    path('total/', get_total), # localhost:8000/api/
    #path('', views.product_list_create_view),
    #path('api/', BookViewSet.as_view())
    path('', include(router.urls)),
]