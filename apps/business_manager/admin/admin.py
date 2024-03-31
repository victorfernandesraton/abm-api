from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin

from apps.business_manager.admin.company_admin import CompanyAdmin
from apps.business_manager.models import Company

neo_admin.register(Company, CompanyAdmin)
