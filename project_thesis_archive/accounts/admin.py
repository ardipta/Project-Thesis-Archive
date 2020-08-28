from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account, StudentProfileUpdate, TeacherProfileUpdate


class AccountAdmin(UserAdmin):
    list_display = (
        'email', 'username', 'employee_id', 'student_id', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'employee_id', 'student_id', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['phone', '']

admin.site.register(Account, AccountAdmin)
admin.site.register(StudentProfileUpdate)
admin.site.register(TeacherProfileUpdate)
