from django.contrib import admin
from .models import Test, Subject, Person, Absenzen, SchoolClass, Thema, Grade
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomStudentAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff', 'klasse',
        'birth', 'street', 'street_number', 'city', 'province', 'code'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('klasse', 'birth', 'street', 'street_number', 'city', 'province', 'code')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('klasse', 'birth', 'street', 'street_number', 'city', 'province', 'code')
        })
    )


admin.site.register(Test)
admin.site.register(Subject)
admin.site.register(Person, CustomStudentAdmin)
admin.site.register(Absenzen)
admin.site.register(SchoolClass)
admin.site.register(Thema)
admin.site.register(Grade)
