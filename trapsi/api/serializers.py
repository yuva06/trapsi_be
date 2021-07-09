from rest_framework import serializers
from trapsi.models import *
from drf_extra_fields.fields import Base64ImageField

class BlogSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
         model = Blog
         fields = "__all__"


class RegistrationApplicationSerializer(serializers.ModelSerializer):
    # image = Base64ImageField()
    class Meta:
         model = RegistrationApplication
         fields = "__all__"
        
class EnquireSerializer(serializers.ModelSerializer):
    # image = Base64ImageField()
    class Meta:
         model = Enquire
         fields = "__all__"

        
class ClientSerializer(serializers.ModelSerializer):
    # image = Base64ImageField()
    class Meta:
         model = Client
         fields = "__all__"

class ClientFormSerializer(serializers.ModelSerializer):
    # image = Base64ImageField()
    class Meta:
         model = ClientForm
         fields = "__all__"