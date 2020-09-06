# Register your models here.
from django.contrib import messages
from django.utils.translation import ngettext
from django.contrib import admin
from datetime import datetime
from .models import SensorType


admin.site.register(SensorType)