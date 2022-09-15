from django.contrib import admin
from App_Login import models

# Register your models here.


class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'dob']


admin.site.register(models.UserProfileModel, UserProfileModelAdmin)
admin.site.register(models.FollowModel)