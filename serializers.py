__author__ = 'PRIYANSH KHANDELWAL'
from rest_framework import serializers
from signalapp.models import employee
from django.contrib.auth.models import User
class login_employee(serializers.Serializer):
    class Meta:
        model=employee

class log_in(serializers.ModelSerializer):
    class Meta:
        model=User




