from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Himanshu
from . serializers import HimanshuSerializer
from django.http import HttpResponse
import datetime

# Create your views here.
def start(request): 
    # fetch date and time 
    now = datetime.datetime.now() 
    # convert to string 
    html = "Time is {}".format(now) 
    # return response 
    return HttpResponse(html)

class himanshuList(APIView):
    def get(self, request):
        e = Himanshu.objects.all()
        serializer = HimanshuSerializer(e,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def add(request,a,b):
    return Response({"Addition":a+b})

@api_view(['GET'])
def sub(request,a,b):
    return Response({"Substration":a-b})

@api_view(['GET'])
def mul(request,a,b):
    return Response({"Multiplication":a*b})

@api_view(['GET'])
def div(request,a,b):
    return Response({"Division":a/b})

@api_view(['GET'])
def pow(request,a,b):
    return Response({"Power":a**b})