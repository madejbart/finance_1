from django.contrib import admin

# Register your models here.
from .models import Company, Land, Realestate

admin.site.register(Company)
admin.site.register(Land)
admin.site.register(Realestate)

