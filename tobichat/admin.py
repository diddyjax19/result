from django.contrib import admin
from django.contrib.auth.models import User, Group
from.models import Dweet, Profile
# Register your models here.

from .models import Profile

# Display profile information page with user admin
class ProfileInline(admin.StackedInline):
    model = Profile

# Only display username field
class UserAdmin(admin.ModelAdmin):
    model = User
    # display only username field
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# unregister group to clean admin interface
admin.site.unregister(Group)
admin.site.register(Dweet)
# register progile
# admin.site.register(Profile)