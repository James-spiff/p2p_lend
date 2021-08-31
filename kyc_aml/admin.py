from django.contrib import admin
from .models import KYCApplication, KYCSetting

# Register your models here.
@admin.register(KYCApplication)
class KYCApplicationAdmin(admin.ModelAdmin):
	pass

@admin.register(KYCSetting)
class KYCSettingAdmin(admin.ModelAdmin):
	pass