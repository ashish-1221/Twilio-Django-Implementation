from import_export import resources,fields
from smsapp1.models import *
from import_export.widgets import ForeignKeyWidget


class UserResource(resources.ModelResource):
    
    class Meta:
        model = User
       