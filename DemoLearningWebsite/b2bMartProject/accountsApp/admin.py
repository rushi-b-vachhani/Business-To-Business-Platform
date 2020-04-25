from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from accountsApp.models import Profile

# Register your models here.


class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
	# list_display = ('username', 'get_userprofile_mobile_number',)
	list_select_related = True
	inlines = (ProfileInline,)

	# def get_userprofile_mobile_number(self, instance):
	# 	# instance is User instance
	# 	return instance.profile.UserMobileNumber





admin.site.unregister(User)
admin.site.register(User, UserAdmin)


