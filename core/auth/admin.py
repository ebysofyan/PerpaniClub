from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            obj.is_staff = True
            obj.save()

admin.site.register(User, UserAdmin)