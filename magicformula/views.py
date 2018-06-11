from django.shortcuts import render
from .models import Market, Company

# Create your views here.
def magicformula(request):
	market = Market.objects.get()
	companies = market.companies.all()
	return render(request, 'magicformula/magic.html', {'market': market, 'companies':companies})


