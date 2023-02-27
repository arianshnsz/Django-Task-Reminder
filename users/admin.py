from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('username', 'phone_number', 'first_name', 'last_name',
                    'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('phone_number', 'username')


admin.site.register(Account, AccountAdmin)
