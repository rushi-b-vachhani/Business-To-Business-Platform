from django.db import models

from accountsApp.models import Profile
from django.core.validators import RegexValidator
# Create your models here.


class Seller(models.Model):
	Profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	
	SellerPromoterCEOName = models.CharField(max_length=30, blank=True, null=True)
	
	fax_regex = RegexValidator(regex=r'^\d{15}$', message="Must be in length of 15")
	SellerFaxNumber = models.CharField(validators=[fax_regex], max_length=15, blank=True, null=True)
	SellerAltFaxNumber = models.CharField(validators=[fax_regex], max_length=15, blank=True, null=True)
	
	def __str__(self):
		return self.Profile.user.username


class Business(models.Model):
	Seller = models.OneToOneField(Seller, on_delete=models.CASCADE)
	
	BusinessCeoName = models.CharField(max_length=30, blank=True)
	BusinessBusinessType = models.CharField(max_length=30, blank=True)
	BusinessOwnershipType = models.CharField(max_length=30, blank=True)
	
	employeeNumber_regex = RegexValidator(regex=r'^\d{0-6}$', message="Must be in length of 6")
	BusinessNumberOfEmployee = models.CharField(validators=[employeeNumber_regex], max_length=6, blank=True)
	
	turnoverNumber_regex = RegexValidator(regex=r'^\d{0-10}$', message="Must be in length of 10")
	BusinessAnnualTurnover = models.CharField(validators=[turnoverNumber_regex], max_length=30, blank=True)
	
	BusinessCompanyLogo = models.ImageField(upload_to="CompanyLogoPicture/%Y/%m/%d", default="DefaultCompanyLogoImage.png", blank=True)
	
	BusinessCompanyWebsite = models.CharField(max_length=100, blank=True)
	
	BusinessCatalogUrl = models.CharField(max_length=100, blank=True, unique= True)
	
	BusinessCardFrontUrl = models.ImageField(upload_to="BusinessCardFrontPicture/%Y/%m/%d", default="DefaultBusinessCardImage.png", blank=True)
	
	BusinessCardBackUrl = models.ImageField(upload_to="BusinessCardBackPicture/%Y/%m/%d", default="DefaultBusinessCardImage.png", blank=True)
	
	def __str__(self):
		return self.Seller.Profile.user.username


class Statutory(models.Model):
	Seller = models.OneToOneField(Seller, on_delete=models.CASCADE)
	
	gstinNumber_regex = RegexValidator(regex=r'^\d{15}]$', message="Must be in length of 15")
	StatutoryGSTIN = models.CharField(validators=[gstinNumber_regex], max_length=15, blank=True)
	
	panNumber_regex = RegexValidator(regex=r'^\d{10}]$', message="Must be in length of 10")
	StatutoryPanNumber = models.CharField(validators=[panNumber_regex], max_length=15, blank=True)
	
	tanNumber_regex = RegexValidator(regex=r'^\d{10}]$', message="Must be in length of 10")
	StatutoryTanNumber = models.CharField(validators=[tanNumber_regex], max_length=15, blank=True)
	
	cinNumber_regex = RegexValidator(regex=r'^\d{21}]$', message="Must be in length of 21")
	StatutoryCinNumber = models.CharField(validators=[cinNumber_regex], max_length=21, blank=True)
	
	dgftNumber_regex = RegexValidator(regex=r'^\d{15}]$', message="Must be in length of 6")
	StatutoryDgftNumber = models.CharField(validators=[dgftNumber_regex], max_length=21, blank=True)


class SellerAddress(models.Model):
	Seller = models.OneToOneField(Seller, on_delete=models.CASCADE)
	
	SellerAddress = models.CharField(max_length=100, blank=True)
	SellerAddressBlockNumber = models.CharField(max_length=10, blank=True)
	SellerAddressStreet = models.CharField(max_length=30, blank=True)
	SellerAddressLocality = models.CharField(max_length=20, blank=True)
	SellerAddressLandMark = models.CharField(max_length=20, blank=True)
	SellerAddressCity = models.CharField(max_length=20, blank=True)
	SellerAddressPinCode = models.CharField(max_length=20, blank=True)
	SellerAddressState = models.CharField(max_length=20, blank=True)
	SellerAddressCountry = models.CharField(max_length=20, blank=True, default='India')
	SellerAddressType = models.CharField(max_length=20, blank=True)
