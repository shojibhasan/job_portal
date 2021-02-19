from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(JobSeekers)
admin.site.register(Employeers)
admin.site.register(JobPost)
