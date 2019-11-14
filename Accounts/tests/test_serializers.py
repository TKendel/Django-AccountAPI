from django.test import TestCase
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

from Accounts.serializers import CustomerSerializer, AccountSerializer
from Accounts.models import Customer, Account


class CustomerSerializerTest(TestCase):
	"""
	Test for the Customer serilaizer
	"""
	@classmethod
	def setUpTestData(cls):
		Customer.objects.create(name="Big",surname="Bob")

	def setUp(self):
		self.customer = Customer.objects.get(id=1)
		self.serializer = CustomerSerializer(instance=self.customer)

	def test_contains_expected_fields(self):
		data = self.serializer.data
		self.assertEqual(set(data.keys()), set(["id","name","surname","balance","accounts"]))

	def test_name_field_content(self):
		data = self.serializer.data
		self.assertEqual(data['name'], self.customer.name)

	def test_surname_field_content(self):
		data = self.serializer.data
		self.assertEqual(data['surname'], self.customer.surname)

	def test_id_field_content(self):
		data = self.serializer.data
		self.assertEqual(data['id'], self.customer.id)

	def test_balance_field_content(self):
		data = self.serializer.data
		self.assertEqual(data['balance'], self.customer.balance)


class AccountSerializerTest(TestCase):
	"""
	Tests for the Account serializer
	"""
	@classmethod
	def setUpTestData(cls):
		customer = Customer.objects.create(name="Big",surname="Bob")
		Account.objects.create(accType=1, credit=50, customer=customer)

	def setUp(self):
		self.account = Account.objects.get(id=1)
		self.serializer = AccountSerializer(instance=self.account)

	def test_contains_expected_fields(self):
		data = self.serializer.data
		self.assertEqual(set(data.keys()), set(["id","accType","credit","account_display","created_at","customer"]))

	def test_id_field_content(self):
		data = self.serializer.data
		self.assertEqual(data['id'], self.account.id)

	def test_credit_field_content(self):
		data = self.serializer.data
		self.assertEqual(data['credit'], self.account.credit)

	def test_accType_field_content(self):
		data = self.serializer.data
		self.assertEqual(data['accType'], self.account.accType)

	"""Since the date is being formated in the serializer,
	the date stored in the model has to be formated in the same way in order for the test to work"""
	def test_created_at_field_content(self):
		data = self.serializer.data
		df = DateFormat(self.account.created_at)
		self.assertEqual(data['created_at'], df.format('d-m-Y'))

	def test_accType_field_content(self):
		data = self.serializer.data
		self.assertEqual(data['accType'], self.account.accType)

