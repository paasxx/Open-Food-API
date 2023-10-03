from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.db import connections
from django.db.utils import OperationalError
import time

from .models import Food
from .serializers import FoodSerializer
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

# get database status and execution time

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getConnection(request):
    start = time.time()
    db_conn = connections['default']
    
    try:
        c = db_conn.cursor()
    except OperationalError:
        connected = False
    else:
        connected = True

    duration = (time.time() - start) * 1000
    serializer = {"database_connection":connected, "time": duration}
    return JsonResponse(serializer)

# get all foods paginated
# example: GET http://localhost:8000/products/?page=4


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getFoods(request):
    
    paginator = PageNumberPagination()
    paginator.page_size = 10
    users = Food.objects.all().order_by('id')
    result_page = paginator.paginate_queryset(users, request)
    serializer = FoodSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)



#add food, not required but helped with the tests
@swagger_auto_schema(methods=['post'], request_body=FoodSerializer)
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addFood(request):
        serializer = FoodSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)


#get single food

@swagger_auto_schema(methods=['put', 'delete'], request_body=FoodSerializer)
@api_view(['GET', 'PUT', 'DELETE' ])
@permission_classes((IsAuthenticated,))
def methodFood(request,pk=1):


    
    def getFood(request,pk):
        try:
            user = Food.objects.get(id=pk)
            serializer = FoodSerializer(user, many=False)
            return Response(serializer.data)
        except:
            return Response('Food id does not exists, try again!')


    #update food
    
    def updateFood(request,pk):
        user = Food.objects.get(id=pk)
        serializer = FoodSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    #delete food
    
    def deleteFood(request,pk):
        try:
            user = Food.objects.get(id=pk)
            user.status = 'trash'
            user.save()
            return Response('Item  status successfully changed to thrash!')
        except:
            return Response('Food id does not exists, try again!')

        
    if request.method == 'GET':
        return getFood(request,pk)
    elif request.method == 'PUT':
        return updateFood(request,pk)
    elif request.method == 'DELETE':
        return deleteFood(request,pk)
   

    