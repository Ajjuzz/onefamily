from django.contrib import admin
from .models import Country, District, Register, State, Contact


admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Register)
admin.site.register(Contact)
