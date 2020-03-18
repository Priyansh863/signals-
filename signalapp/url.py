__author__ = 'PRIYANSH KHANDELWAL'
from rest_framework import serializers
from signalapp.views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'employee_viewset',employee_viewset,basename='employee_viewset')
urlpatterns = router.urls