from django.db import models
from decimal import Decimal


class Customer(models.Model):
	name = models.CharField(max_length = 255, blank = False, default='')
	surname = models.CharField(max_length = 255, blank = False, default='')
	balance = models.DecimalField(max_digits = 6, decimal_places = 2, default=Decimal('0.00'))
	created_at = models.DateTimeField( auto_now_add = True )
	updated_at = models.DateTimeField( auto_now = True )

	def __str__( self ):
		return self.name


class Account(models.Model):
	SAVING = 1
	INSURANCE = 2
	Account_Type = [
		(1, 'Saving'),
		(2, 'Insurance'),
	]
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="accounts", blank = False, default='')
	accType = models.PositiveSmallIntegerField(choices = Account_Type)
	credit = models.DecimalField(max_digits = 8, decimal_places = 2, default = Decimal('0.00'))
	created_at = models.DateTimeField( auto_now_add = True )
	updated_at = models.DateTimeField( auto_now = True )

	def __str__(self):
		return "%s, %s account" % (self.customer.name, self.customer.surname)