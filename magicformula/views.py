from django.shortcuts import render
from .models import Market, Company
from django_tables2 import RequestConfig
from .tables import CompaniesTable

# Create your views here.
def magicformula(request):
	market = Market.objects.get()
	companies = market.companies.all()
	table = CompaniesTable(market.companies.all())
	return render(request, 'magicformula/magic.html', {'market': market, 'table':table})


