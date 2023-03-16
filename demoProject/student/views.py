from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from django.utils import timezone


# Create your views here.

def index(request):
    return HttpResponse("Student App test")

class StudentApiView(APIView):

   



    def post(self, request, *args, **kwargs):

        '''
         Create the student model with given Student data
        '''
        data = {
            "first_Name":request.data.get("first_Name"),
            "last_Name": request.data.get("last_Name"),
            "batch": request.data.get("batch"),
            "creation_date": timezone.now().date()
            }
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
            
        
            




