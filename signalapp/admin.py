from django.contrib import admin
from .models import *

from rest_framework.authtoken.models import Token
#admin.site.register(Token)

admin.site.register(employee)
admin.site.register(admin1)

# Register your models here.
