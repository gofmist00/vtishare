from django.contrib import admin
from django.contrib.auth.models import Group
from user.models import User, LevelAndSection
from user.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('student_number','email','first_name', 'last_name','level_and_section','is_student','is_officer')}
        ),
    )
    model = User
    list_display = ('email','first_name', 'last_name')
    list_filter = ('email','first_name', 'last_name')
    fieldsets = (
        (None, {
            'fields':(
                'student_number','email','first_name', 'last_name','level_and_section','is_student','is_officer','password'
            )
        }),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        }),
        ('Permissions',{
            'fields':(
                'is_staff',
                'is_active',
                'email_verified',
            )
        })
    )
    search_fields = ('email',)
    ordering = ('id',)

admin.site.register(User, UserAdmin)
admin.site.register(LevelAndSection)