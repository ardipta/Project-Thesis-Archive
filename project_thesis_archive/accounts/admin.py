from django.contrib import admin
from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'email', 'fullname', 'employee_id', 'student_id', 'role', 'is_admin', 'is_staff'
    ]
    search_fields = ('email', 'employee_id', 'student_id')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['user', 'phone', ]


admin.site.register(Account, AccountAdmin)
# admin.site.register(StudentProfile, StudentAdmin)
# admin.site.register(TeacherProfile)
