from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, User_Delivery_Address, User_Payment_Address, User_Credit_Card, User_PayPal, User_Debit

# Register your models here.


class ProfileAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'username', 'last_login', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login',)
    ordering = ('last_login',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class User_Delivery_AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'delivery_street',
                    'delivery_house_number', 'delivery_city', 'delivery_plz')


class User_Payment_AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_street',
                    'payment_house_number', 'payment_city', 'payment_plz')


class User_Credit_CardAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner_first_name',
                    'owner_last_name', 'card_number',
                    'expiration_date_month', 'expiration_date_year',
                    'security_code')


class User_PayPalAdmin(admin.ModelAdmin):
    list_display = ('user', 'paypal_mail', 'paypal_password')


class User_DebitAmin(admin.ModelAdmin):
    list_display = ('user', 'debit_first_name',
                    'debit_last_name', 'iban', 'bic')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(User_Delivery_Address, User_Delivery_AddressAdmin)
admin.site.register(User_Payment_Address, User_Payment_AddressAdmin)
admin.site.register(User_Credit_Card, User_Credit_CardAdmin)
admin.site.register(User_PayPal, User_PayPalAdmin)
admin.site.register(User_Debit, User_DebitAmin)
