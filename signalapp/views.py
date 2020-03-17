from django.core.mail import send_mail
from rest_framework.response import Response
from django.http import HttpResponse
from signalapp.models import employee
p=5
for i in range(0,5):
    def xyz(request):




        x="arushijhalani9220@gmail.com"
        #y="priyanshjhalani30@gmail.com"
        sender="priyanshjhalani0@gmail.com"
        #sender="priyanshjhalani30@gmail.com"

        send_mail(
        'Subject here',
        '''The Lion and the Mouse

    One of Aesop's Fables, numbered 150 in the Perry Index

    The Lion and the Mouse is one of Aesop's Fables, numbered 150 in the Perry Index. There are also Eastern variants of the story, all of which''',
        sender,
        [x],
        fail_silently=False,
        )
        return HttpResponse("ok")








class lietset(vietset)





'''
class login_employee(viewsets.ViewSet):
    def create(self,request):
        serializers=login_employee1
        if serializers.is_valid():
            flag=serializers.data['key']
            flag1=serializers.data['password']
            p=employee.objects.all()
            try:
                a=employee.objects.get(hod_email=flag)

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
            return Response(serializers.errors)

'''