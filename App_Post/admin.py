from django.contrib import admin
from App_Post import models

# Register your models here.

admin.site.register(models.PostModel)
admin.site.register(models.LikeModel)
