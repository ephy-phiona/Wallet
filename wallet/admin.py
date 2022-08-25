
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
from .models import Transaction

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","Gender","age","email","nationality",
    "phonenumber","marital_status","signature","employment_status","employment_status","profile_picture")
    search_fields=("first_name","last_name","Gender","address","age","email","nationality",
    "phonenumber","marital_status","signature","employment_status","employment_status","profile_picture")
admin.site.register(Customer, CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=("user_name","balance","amount","pin","date","wallet_type",)
    search_fields=("user_name","balance","amount","pin","customer","date","wallet_type")
admin.site.register(Wallet,WalletAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("date","transaction")
    search_fields=("date","transaction")
admin.site.register(Receipt,ReceiptAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=("name","account_number","account_type","savings","destination")
    search_fields=("name","account_number","account_type","savings","destination")
admin.site.register(Account,AccountAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_type","amount","date_time","loan_terms","payment_due_date",
    "guaranter","balance","duration","interest_rate","loan_status")
    search_fields=("loan_type","amount","date_time","loan_terms","payment_due_date",
    "guaranter","balance","duration","interest_rate","loan_status")
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("points","date","transaction")
    search_fields=("points","date","transaction")
admin.site.register(Reward,RewardAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("message","date_created","notification_status","image")
    search_fields=("message","date_created","notification_status","image")
admin.site.register(Notification,NotificationAdmin)

class Third_partyAdmin(admin.ModelAdmin):
    list_display=("name","email","id_number","status_third","account","phone_number",
    "amount")
    search_fields=("name","email","id_number","status_third","account","phone_number",
    "amount")
admin.site.register(Third_party,Third_partyAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=("card_number","card_name","card_type","expiry_date","security_code",
    "date_ofissue","account_number")
    search_fields=("card_number","card_name","card_type","expiry_date","security_code",
    "date_ofissue","account")
admin.site.register(Card,CardAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_charge","transaction_code","wallet","transaction_amount",
    "receipt","transaction_type","transaction_datetime","status_T")
    search_fields=("transaction_charge","transaction_code","wallet","transaction_amount",
    "receipt","transaction_type","transaction_datetime","status_T")
admin.site.register(Transaction,TransactionAdmin)



