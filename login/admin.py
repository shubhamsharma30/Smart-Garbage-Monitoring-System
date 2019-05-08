# -*- coding: utf-8 -*-
from django.contrib import admin
#from login.models import UserProfileInfo, User
from login.models import D_Details
from login.models import C_Details
from login.models import Trashcan1

# Register your models here.
#admin.site.register(UserProfileInfo)
admin.site.register(D_Details)
admin.site.register(C_Details)
admin.site.register(Trashcan1)
