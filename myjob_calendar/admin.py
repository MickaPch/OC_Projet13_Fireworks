from django.contrib import admin
from myjob_calendar.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
