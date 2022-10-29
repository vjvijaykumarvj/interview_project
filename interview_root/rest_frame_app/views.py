from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ViewSet
from.models import Database
from.serializer import Data_serializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView

########################### 1st way using Model View Set ################################
# Create your views here.

class Employee_crud(ModelViewSet):
    serializer_class = Data_serializer      # This is fastly excecute the code purpose used
    queryset = Database.objects.all()

##############################################################################################

###################### 2nd way using View Set ################################################
'''
class Employee_crud(ViewSet):
    def create(self,request,*args,**kwargs):
        # get the input data from client
        emp_json = request.data
        # apply the serialization operation
        emp_serializer = Data_serializer(data=emp_json)
        if emp_serializer.is_valid():
            emp_serializer.save()
        return Response(emp_serializer.data)
    def list(self,request,*args,**kwargs):
        # get the all records from database
        emp_qs = Database.objects.all()
        # aply the serializer operation
        em_seailizer = Data_serializer(emp_qs,many=True)
        # return back convert the dict formate
        emp_dict = em_seailizer.data
        return Response(emp_dict)
    def update(self,request,*args,**kwargs):
        # get the data from client
        emp_json = request.data
        # get the all the record from database
        emp = Database.objects.all()
        # apply the serializer operation convert purpose
        emp_serializer  =Data_serializer(instance=emp,data=emp_json)
        if emp_serializer.is_valid():
            # save the data
            emp_serializer.save()
        return Response(emp_serializer.data)
    def retrieve(self,request,pk,*args,**kwargs):
        # get the single record from database
        emp = Database.objects.get(id=pk)
        ## apply the serializer operation convert purpose
        emp_serializer = Data_serializer(emp)
        return Response(emp_serializer)
    def delete(self,request,pk,*args,**kwargs):
        # get the single record from database
        emp = Database.objects.get(id=pk)
        # delete the record 
        emp.delete()
        # response messege back to client
        return Response({'messege':'Delete data successfully'})
'''


