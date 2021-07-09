from django.shortcuts import render
from .serializers import *
from trapsi.models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework import permissions, authentication

class BlogListView(generics.ListAPIView):
     queryset = Blog.objects.all()
     serializer_class = BlogSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]

class BlogDetialView(generics.RetrieveAPIView):
     queryset = Blog.objects.all()
     serializer_class = BlogSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]

class RegistrationApplicationListView(generics.ListCreateAPIView):
     queryset = RegistrationApplication.objects.all()
     serializer_class = RegistrationApplicationSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]

class RegistrationApplicationDetialView(generics.RetrieveAPIView):
     queryset = RegistrationApplication.objects.all()
     serializer_class = RegistrationApplicationSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]
     
class EnquireListView(generics.ListCreateAPIView):
     queryset = Enquire.objects.all()
     serializer_class = EnquireSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]

class EnquireDetialView(generics.RetrieveAPIView):
     queryset = Enquire.objects.all()
     serializer_class = EnquireSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]

class ClientListView(generics.ListCreateAPIView):
     queryset = Client.objects.all()
     serializer_class = ClientSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]

class ClientDetialView(generics.RetrieveAPIView):
     queryset = Client.objects.all()
     serializer_class = ClientSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]

class ClientFormListView(generics.ListCreateAPIView):
     queryset = ClientForm.objects.all()
     serializer_class = ClientFormSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]

class ClientFormDetialView(generics.RetrieveAPIView):
     queryset = ClientForm.objects.all()
     serializer_class = ClientFormSerializer

     permission_classes=[permissions.AllowAny,]
     authentication_classes=[authentication.TokenAuthentication]