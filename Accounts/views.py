from django.shortcuts import HttpResponseRedirect
from rest_framework import status, renderers, generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import SuspiciousOperation
from decimal import Decimal

from .models import Account,Customer
from .serializers import AccountSerializer,CustomerSerializer


class CustomerList(APIView):
	"""
	View for listing all the current customers
	"""
	renderer_classes = [TemplateHTMLRenderer]
	template_name = "Customer/index.html"

	def get(self, request):
		customers = Customer.objects.all()

		serializer = CustomerSerializer(customers, many = True)
		return Response({'customers': serializer.data})


class CreateAccount(APIView):
	"""
	View for adding an account to a selected customer
	"""	
	renderer_classes = [TemplateHTMLRenderer]
	template_name = "Account/new.html"

	def get_object(self, pk):
		return Customer.objects.get(pk = pk)

	def get(self, request, pk):
		customer = self.get_object(pk)
		form = AccountSerializer()
		serializer = CustomerSerializer(customer)
		return Response({"AccForm": form, "customer": serializer.data })

	def post(self, request, pk):
		customer = self.get_object(pk)

		#Validation
		if Decimal(request.data["credit"]) > customer.balance:
			raise SuspiciousOperation("Credit ammount is bigger then your current balance")
		elif Decimal(request.data["credit"]) <= Decimal('0.00'):
			raise SuspiciousOperation("You cant open new account by depositing negative or 0 money")
		else:
			customer.balance = customer.balance - Decimal(request.data["credit"])
			serializer = AccountSerializer(data = request.data)

		if serializer.is_valid():
			customer.save()
			serializer.save(customer_id = customer.id)
			return HttpResponseRedirect("/Accounts/")

		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	
class CustomerDetail(APIView):
	"""
	View for displaying details about a selected customer
	"""
	renderer_classes = [TemplateHTMLRenderer]
	template_name = "Customer/Detail.html"

	def get_object(self, pk):
		return Customer.objects.get(pk = pk)

	def get(self, request, pk):
		customer = self.get_object(pk)

		#A dictionary of account types a customer has, used for the display of made transactions
		account_dict = {}
		for account in customer.accounts.all(): 
			account_dict[account.accType] = account.get_accType_display

		serializer = CustomerSerializer(customer)
		
		return Response({'Customer': serializer.data, "Accounts": account_dict})
