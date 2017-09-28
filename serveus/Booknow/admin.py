from django.contrib import admin
from .models import customer
from .models import service_providers
from .models import service_list
from .models import booking



admin.site.register(service_providers)
admin.site.register(service_list)
admin.site.register(booking)
admin.site.register(customer)
