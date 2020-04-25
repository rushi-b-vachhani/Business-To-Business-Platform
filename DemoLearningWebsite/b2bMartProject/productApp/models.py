from django.db import models
from sellerAccountApp.models import Seller
# Create your models here.
from django.core.validators import RegexValidator


class ProductCurrency(models.Model):
	ProductCurrencyName = models.CharField(max_length=20, blank=False, null=False)


class ProductMeasuringUnit(models.Model):
	ProductMeasuringUnitName = models.CharField(max_length=20, blank=False, null=False)


class IndustryCategory(models.Model):
	IndustryCategoryName = models.CharField(max_length=30, blank=False, null=False)
	

class ExportCategory(models.Model):
	IndustryCategory = models.ManyToManyField(IndustryCategory)
	
	ExportCategoryName = models.CharField(max_length=50, blank=False, null=False)


class ImpCategory(models.Model):
	ExportCategory = models.ForeignKey(ExportCategory, on_delete=models.CASCADE)
	
	ImpCategoryName = models.CharField(max_length=50, blank=False, null=False)


# https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_one/ ----- REFER For Examples Many to One
class Product(models.Model):
	ImpCategory = models.ManyToManyField(ImpCategory)
	ProductMeasuringUnit = models.ForeignKey(ProductMeasuringUnit, on_delete=models.CASCADE, blank=True, null=True)  # dependant ------1
	ProductCurrency = models.ForeignKey(ProductCurrency, on_delete=models.CASCADE, blank=True, null=True)
	Seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=False, blank=False)
	
	ProductName = models.CharField(max_length=50, null=False, blank=False)
	ProductImageUrl = models.ImageField(upload_to="ProductPicture/%Y/%m/%d", default="ProductPicture/2020/04/24/DefaultProductPicture.png", blank=True, null=True)
	ProductPrice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # dependant ------1
	ProductDescription = models.TextField(max_length=150, blank=True, null=True)
	ProductMinimumOrderQuantity = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	ProductProductionCapacity = models.CharField(max_length=50, blank=True, null=True)
	ProductCode = models.CharField(max_length=20, blank=True, null=True)
	ProductDeliveryTime = models.CharField(max_length=20, blank=True, null=True)
	ProductPackagingDetails = models.CharField(max_length=500, blank=True, null=True)
	
	
class SpecificationType(models.Model):
	SpecificationTypeName = models.CharField(max_length=20, blank=False, null=False)


class ProductSpecification(models.Model):
	ProductSpecificationName = models.CharField(max_length=50, blank=False, null=False)
	SpecificationType_id = models.ForeignKey(SpecificationType, on_delete=models.CASCADE, null=False, blank=False)


class SpecificationValue(models.Model):
	SpecificationValueValue = models.CharField(max_length=50, blank=False, null=False)
	ProductSpecification_id = models.ForeignKey(ProductSpecification, on_delete=models.CASCADE, null=False, blank=False)
	Product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
