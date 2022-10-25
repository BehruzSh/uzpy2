from django.contrib import admin

# Register your models here.
class KiyimAdmin(admin.ModelAdmin):
    list_display = ('id','nomi','turi','ulcham','narxi')
from .models import *
admin.site.register(Xaridor)
admin.site.register(Category)
admin.site.register(Kiyim,KiyimAdmin)

