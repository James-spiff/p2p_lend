from django.contrib import admin
from .models import KYCApplication, KYCSetting

# Register your models here.
@admin.register(KYCApplication)
class KYCApplicationAdmin(admin.ModelAdmin):
	
	def has_add_permission(self, obj):  #This doesn't allow staff access the add functionality on the KYC application by default it's set to True
		return False 

@admin.register(KYCSetting)
class KYCSettingAdmin(admin.ModelAdmin):
	pass