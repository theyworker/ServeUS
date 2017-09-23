from django.contrib import admin
from .models import customer, service_list,service_providers,booking, admin1

admin.site.register(customer)
admin.site.register(service_list)
admin.site.register(service_providers)
admin.site.register(booking)
admin.site.register(admin1)
