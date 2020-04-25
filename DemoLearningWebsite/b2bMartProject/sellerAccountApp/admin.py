from django.contrib import admin

from .models import Seller
from .models import Business
from .models import Statutory
# Register your models here.


class SellerAdmin(admin.ModelAdmin):
	list_display = ('Profile', 'SellerPromoterCEOName', 'SellerFaxNumber', 'SellerAltFaxNumber',)


admin.site.register(Seller, SellerAdmin)

admin.site.register(Business)
admin.site.register(Statutory)
