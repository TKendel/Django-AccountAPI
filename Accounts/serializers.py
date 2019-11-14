from rest_framework import serializers
from decimal import Decimal

from .models import Account, Customer


class AccountSerializer(serializers.ModelSerializer):
	"""
	Serializer for account data
	"""
	account_display = serializers.CharField(source = "get_accType_display", read_only = True)
	created_at = serializers.DateTimeField(format = "%d-%m-%Y", read_only = True)
	accType = serializers.ChoiceField(choices = [(1, 'Saving'), (2, 'Insurance')], label = "What kind of account would you like")
	credit = serializers.DecimalField(decimal_places = 2, max_digits = 8, label= "How much would you like to deposit ?")

	class Meta:
		model = Account
		fields = ["id", "accType", "credit", "account_display", "created_at", "customer"]
		read_only_fields = ["customer", "account_display"]


class CustomerSerializer(serializers.ModelSerializer):
	"""
	Serializer for customer data
	"""
	accounts = AccountSerializer(many = True, read_only = True)

	class Meta:
		model = Customer
		fields = ["id", "name", "surname", "balance", "accounts"]
