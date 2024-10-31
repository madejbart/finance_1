from django.contrib import admin

# Register your models here.
from .models import Company, Land, Realestate, Profile, Result

admin.site.register(Company)
admin.site.register(Land)
admin.site.register(Realestate)
admin.site.register(Profile)
admin.site.register(Result)

