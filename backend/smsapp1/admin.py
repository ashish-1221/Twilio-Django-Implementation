from django.contrib import admin
from .models import User,Group
from import_export.admin import ImportExportModelAdmin
from .resource import UserResource

# Register your models here.
class UserAdmin(ImportExportModelAdmin):
    resource_class = [UserResource]
    


admin.site.register(User,UserAdmin)
admin.site.register(Group)
# admin.site.register(SmsSupport)