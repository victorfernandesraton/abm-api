from django.contrib.admin import ModelAdmin


class CompanyAdmin(ModelAdmin):
    list_display = ["label", "description"]
