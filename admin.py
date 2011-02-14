from django.contrib import admin
from uwregistry.models import Service

class ServiceAdmin(admin.ModelAdmin):
    exclude = ('user_voice_categories',)

admin.site.register(Service,ServiceAdmin)
