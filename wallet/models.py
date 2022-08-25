from django.db import models
import datetime


# Create your models here.

class Customer(models.Model):
    first_name=models.CharField(max_length=15,null=True)
    last_name=models.CharField(max_length=15,null=True)
    Gender=models.CharField(max_length=1,null=True)
    address=models.TextField()
    age=models.PositiveSmallIntegerField(default= False)
    email=models.EmailField(max_length=20,null=True)
    nationality=models.CharField(max_length=10,null=True)
    phonenumber=models.CharField(max_length=15,null=True)
    marital_status=models.CharField(max_length=30, null = True)
    signature=models.ImageField(default = False)
    employment_status=models.BooleanField(default=False)
    profile_picture=models.ImageField(default = False)


class Wallet(models.Model):
    user_name=models.CharField(max_length=20, null = True)
    balance=models.IntegerField()
    amount=models.IntegerField()
    pin=models.PositiveSmallIntegerField()
    Customer=models.ForeignKey(Customer,default=1,on_delete=models.CASCADE,) 
    date=models.DateTimeField(default= datetime.datetime.now)
    wallet_type=models.CharField(max_length=30, blank = True)


class Account(models.Model):
    name=models.CharField(max_length=30, blank= True)
    account_number=models.IntegerField()
    account_type=models.CharField(max_length=30 ,blank= True, default=False)
    savings=models.IntegerField(default= False)
    destination=models.CharField(max_length=30, blank=True)
    
class Transaction(models.Model):
    transaction_charge=models.IntegerField(default=False)
    transaction_code=models.CharField(max_length=30, blank= True, default= False)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Transaction_wallet', blank = True, default= False)
    transaction_amount=models.IntegerField(default= False)
    receipt=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Transaction_receipt', blank = True, default= False)
    transaction_type=models.CharField(max_length=30, blank= True, default= False)
    transaction_datetime=models.DateTimeField(default=datetime.datetime.now)
    status_T=models.CharField(max_length=20, blank= True)

class Card(models.Model):
    card_number=models.IntegerField(default=False)
    card_name=models.CharField(max_length=30, blank= True)
    card_type=models.CharField(max_length=30, blank= True, default=False)
    expiry_date=models.DateTimeField(default= datetime.datetime.now)
    security_code=models.IntegerField(default= False)
    date_ofissue=models.DateTimeField(default= datetime.datetime.now)
    account=models.IntegerField(default= False)

class Third_party(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    id_number=models.CharField(max_length=30)
    status_third=models.CharField(max_length=30,default=False)
    account=models.ForeignKey('account',on_delete=models.CASCADE,related_name='Third_party_account')
    phone_number=models.CharField(max_length=30)
    amount=models.IntegerField()
    trasaction_cost=models.IntegerField()

class Notification(models.Model):
    message=models.TextField(max_length=50, blank = True)
    date_created=models.DateField(default= datetime.datetime.now)
    recipient=models.CharField(max_length=20, blank = True)
    notification_status=models.CharField(max_length=50, blank = True)
    image=models.ImageField(default = False)

class Receipt(models.Model):
    date=models.DateTimeField(default= datetime.datetime.now)
    transaction=models.IntegerField(default= False)

class Loan(models.Model):
    loan_type=models.CharField(max_length=30, blank = True,default= False)
    amount=models.IntegerField(default= False)
    date_time=models.DateTimeField(default= datetime.datetime.now)
    loan_terms=models.CharField(max_length=20, blank = True)
    payment_due_date=models.DateTimeField(default= datetime.datetime.now)
    guaranter=models.CharField(max_length=20, blank= True)
    balance=models.IntegerField(default= False)
    duration=models.CharField(max_length=30, null= True)
    interest_rate=models.IntegerField(default= False)
    loan_status=models.CharField(max_length=30, null = True)

class Reward(models.Model):
    
    points=models.IntegerField(default=False)
    date=models.DateTimeField(default= datetime.datetime.now)
    transaction=models.ForeignKey(Transaction, blank= True,on_delete=models.CASCADE,related_name='Reward_Transaction')




