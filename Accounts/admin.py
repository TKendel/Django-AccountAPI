from django.contrib import admin
from .models import Account,Customer

"""
For djangos admin site
"""
admin.site.register(Account)
admin.site.register(Customer)