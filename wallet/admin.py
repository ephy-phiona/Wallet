from django.contrib import admin
from .models import Customer
from .models import Wallet
from .models import Receipt
from .models import Account
from .models import Loan
from .models import Reward
from .models import Notification
from .models import Card
from .models import Third_party

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","Gender","address","age","email","nationality",
    "phonenumber","marital_status","signature","employment_status","employment_status","profile_picture")
    search_fields=("first_name","last_name","Gender","address","age","email","nationality",
    "phonenumber","marital_status","signature","employment_status","employment_status","profile_picture")
admin.site.register(Customer, CustomerAdmin)

admin.site.register(Wallet)
admin.site.register(Receipt)
admin.site.register(Account)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Notification)
admin.site.register(Third_party)
admin.site.register(Card)
admin.site.register(Transaction)



