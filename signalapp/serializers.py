__author__ = 'PRIYANSH KHANDELWAL'
from rest_framework import serializers
from signalapp.models import employee
from django.contrib.auth.models import User
class login_employee(serializers.Serializer):
    pass



class log_in(serializers.ModelSerializer):
    username=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100)





class employee_serial(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'