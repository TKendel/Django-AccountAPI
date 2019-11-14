from django.test import TestCase
from decimal import Decimal

from Accounts.models import Customer, Account


class CustomerModelTest(TestCase):
	"""
	Tests for the Customer model
	"""
	@classmethod
	def setUpTestData(cls):
		Customer.objects.create(name="Big", surname="Bob")

	def test_name_label(self):
		customer = Customer.objects.get(id=1)
		field_label = customer._meta.get_field('name').verbose_name
		self.assertEqual(field_label, 'name')

	def test_name_max_length(self):
		customer = Customer.objects.get(id=1)
		max_length = customer._meta.get_field('name').max_length
		self.assertEqual(max_length, 255)

	def test_surname_label(self):
		customer = Customer.objects.get(id=1)
		field_label = customer._meta.get_field('surname').verbose_name
		self.assertEqual(field_label, 'surname')

	def test_surname_max_length(self):
		customer = Customer.objects.get(id=1)
		max_length = customer._meta.get_field('surname').max_length
		self.assertEqual(max_length, 255)

	def test_object_name_is_name_comma_surname(self):
		customer = Customer.objects.get(id=1)
		expected_object_name = customer.name
		self.assertEqual(expected_object_name, str(customer))

	def test_balance_label(self):
		customer = Customer.objects.get(id=1)
		balance = customer._meta.get_field('balance').verbose_name
		self.assertEqual(balance, ('balance'))

	def test_balance_inital(self):
		customer = Customer.objects.get(id=1)
		balance = customer.balance
		self.assertEqual(balance, Decimal("0.00"))

	def test_balance_max_digits(self):
		customer = Customer.objects.get(id=1)
		balance = customer._meta.get_field('balance').max_digits
		self.assertEqual(balance, 6)

	def test_balance_max_decimal_places(self):
		customer = Customer.objects.get(id=1)
		balance = customer._meta.get_field('balance').decimal_places
		self.assertEqual(balance, 2)

	def test_created_at_label(self):
		customer = Customer.objects.get(id=1)
		created_at_label = customer._meta.get_field('created_at').verbose_name
		self.assertEqual(created_at_label, ("created at"))

	def test_updated_at_label(self):
		customer = Customer.objects.get(id=1)
		updated_at_label = customer._meta.get_field('updated_at').verbose_name
		self.assertEqual(updated_at_label, ("updated at"))


class AccountModelTest(TestCase):
	"""
	Tests for the Account model
	"""
	@classmethod
	def setUpTestData(cls):
		customer = Customer.objects.create(name="Big", surname="Bob")
		Account.objects.create(accType=1, credit = 50, customer = customer)

	def test_accType_label(self):
		account = Account.objects.get(id=1)
		accType_label = account._meta.get_field('accType').verbose_name
		self.assertEqual(accType_label,('accType'))

	def test_customer_label(self):
		account = Account.objects.get(id=1)
		accType_label = account._meta.get_field('customer').verbose_name
		self.assertEqual(accType_label, "customer")

	def test_credit_label(self):
		account = Account.objects.get(id=1)
		credit_label = account._meta.get_field('credit').verbose_name
		self.assertEqual(credit_label,('credit'))

	def test_balance_inital(self):
		account = Account.objects.get(id=1)
		credit = account.credit
		self.assertTrue(credit > Decimal("0.00"))

	def test_balance_max_digits(self):
		account = Account.objects.get(id=1)
		credit = account._meta.get_field('credit').max_digits
		self.assertEqual(credit, 8)

	def test_credit_max_decimal_places(self):
		account = Account.objects.get(id=1)
		credit = account._meta.get_field('credit').decimal_places
		self.assertEqual(credit, 2)

	def test_created_at_label(self):
		account = Account.objects.get(id=1)
		created_at_label = account._meta.get_field('created_at').verbose_name
		self.assertEqual(created_at_label, ("created at"))

	def test_updated_at_label(self):
		account = Account.objects.get(id=1)
		updated_at_label = account._meta.get_field('updated_at').verbose_name
		self.assertEqual(updated_at_label, ("updated at"))

	def test_object_name_is_name_comma_surname(self):
		account = Account.objects.get(id=1)
		expected_object_name = "%s, %s account" % (account.customer.name, account.customer.surname)
		self.assertEqual(expected_object_name, str(account))
