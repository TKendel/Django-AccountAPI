from django.test import TestCase
from django.urls import reverse

from Accounts.models import Customer, Account
from Accounts.views import CustomerList, CreateAccount, CustomerDetail


class CustomerListViewTest(TestCase):
	"""
	Tests for the Customer List view
	"""
	@classmethod
	def setUpTestData(cls):
		number_of_customers = 4

		for customer_id in range(1,number_of_customers):
			Customer.objects.create(name="test{customer_id}", surname="test{customer_id}")

	def test_view_url_exists_at_desired_location(self):
		response = self.client.get('/Accounts/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_accessible_by_name(self):
		response = self.client.get(reverse('Customers'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse("Customers"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'Customer/index.html')

class CreateAccountViewTest(TestCase):
	"""
	Tests for the Create Account view
	"""
	@classmethod
	def setUpTestData(cls):
		customer = Customer.objects.create(name="Big", surname="Bob")
		Account.objects.create(accType=1, credit = 50, customer = customer)

	def test_view_url_exists_at_desired_location(self):
		customer = Customer.objects.get(id=1)

		response = self.client.get('/Accounts/New/{}'.format(customer.id))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		customer = Customer.objects.get(id=1)

		response = self.client.get('/Accounts/New/{}'.format(customer.id))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'Account/new.html')

class CustomerDetailViewTest(TestCase):
	"""
	Tests for the Customer Detail view
	"""
	@classmethod
	def setUpTestData(cls):
		customer = Customer.objects.create(name="Big", surname="Bob")
	
	def test_view_url_exists_at_desired_location(self):
		customer = Customer.objects.get(id=1)

		response = self.client.get('/Accounts/Detail/{}'.format(customer.id))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		customer = Customer.objects.get(id=1)
		
		response = self.client.get('/Accounts/Detail/{}'.format(customer.id))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'Customer/Detail.html')