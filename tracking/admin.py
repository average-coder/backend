from django.conf import settings
from django.contrib import admin
from .models import APIRequestLog

admin.site.register(APIRequestLog)
