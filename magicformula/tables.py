import django_tables2 as tables
from .models import Company

class CompaniesTable(tables.Table):
	class Meta:
		model = Company
		template_name = 'django_tables2/bootstrap.html'
		exclude = ('id', 'ticker')	

