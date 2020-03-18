from django.core.mail import send_mail
from rest_framework.response import Response
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from rest_framework import viewsets
from signalapp.models import employee
from django.contrib.auth.models import User
from signalapp.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
p=5
for i in range(0,5):
    def xyz(request):
        templt=render_to_string('xyz.html',{'Name':'karan'})





        x="deykaran07@gmail.com"
        y="jhalanipriyansh25@gmail.com"
        #y="priyanshjhalani30@gmail.com"
        sender="priyanshjhalani0@gmail.com"
        #sender="priyanshjhalani30@gmail.com"

        send_mail(
        'Subject here',
        ' ',
        sender,
        [x,y],
        fail_silently=False,html_message=templt
        )
        return HttpResponse("ok")















'''class login_employee(viewsets.ViewSet):
    def create(self,request):
        serializers=log_in(data=request.data)
        if serializers.is_valid():
            flag=serializers.data['username']
            flag1=serializers.data['password']


            try:
                p=employee.objects.get()
                p=User.objects.get(username=)


            except:
                try:

                    a=employee.objects.get(hod_id=flag)
                except:
                    return Response('Invalid id')
            if a.check_password(flag1) ==True:
                return Response('Login Successfully')
            else:
                return Response('Password not valid ')
        else:
            return Response(serializers.errors)'''

class employee_viewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        u=self.request.user
        if x.type==admin:
            employee.objects.all()
        else:
            employee.objects.filter(id=1)

        print('\n\n\n',u,' \n\n')


        x=employee.objects.filter(id=1)
        return x

    serializer_class = employee_serial
    http_method_names = ['get','post','patch']