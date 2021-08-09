from django.contrib import admin
from appliances.models import Appliance, Skill, Mission


@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    pass
