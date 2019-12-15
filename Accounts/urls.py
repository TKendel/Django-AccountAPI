from django.urls import path
from rest_framework.schemas import get_schema_view

from Accounts import views


urlpatterns = [
	path('', views.CustomerList.as_view(), name = "Customers"),
	path('New/<int:pk>', views.CreateAccount.as_view(), name = "NewAccount"),
	path('Detail/<int:pk>', views.CustomerDetail.as_view(), name = "Detail"),
    #schema view for the swagger definition
	path('openapi', get_schema_view(
        title = "Bank Project",
        description = "Open API for the bank account",
        version = "1.0.0",
    ), name = "openapi-schema"),
]