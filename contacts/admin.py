from django.contrib import admin
from contacts.models.models import Company, Contact


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
