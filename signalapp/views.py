from django.core.mail import send_mail
from rest_framework.response import Response
from django.http import HttpResponse
p=5
def xyz(request):
    

    x="deykaran07@gmail.com"
    y="priyanshjhalani30@gmail.com"
    sender="priyanshjhalani0@gmail.com"
    send_mail(
    'Subject here',
    '''The Lion and the Mouse

One of Aesop's Fables, numbered 150 in the Perry Index

The Lion and the Mouse is one of Aesop's Fables, numbered 150 in the Perry Index. There are also Eastern variants of the story, all of which''',
    sender,
    [x,y],
    fail_silently=False,
    )
    return HttpResponse("rxctfgvybunjf vbn")