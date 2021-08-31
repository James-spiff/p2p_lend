from django.contrib import admin
from .models import KycApplication

# Register your models here.
@admin.register(KYCApplication)
class KycApplicationAdmin(admin.ModelAdmin):
	pass