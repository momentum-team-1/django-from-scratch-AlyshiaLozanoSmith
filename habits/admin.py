from django.contrib import admin
from .models import Habit, DailyRecord

admin.site.register(Habit)
admin.site.register(DailyRecord)