from django.urls import path

from Accounts import views


urlpatterns = [
	path('', views.CustomerList.as_view(), name = "Customers"),
	path('New/<int:pk>', views.CreateAccount.as_view(), name = "NewAccount"),
	path('Detail/<int:pk>', views.CustomerDetail.as_view(), name = "Detail")
]