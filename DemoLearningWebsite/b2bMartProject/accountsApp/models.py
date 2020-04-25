from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

# if you have  doubt on how one to one relation ship works then you should read following answer
# The OneToOneField evolved in Django after 'ForeignKey'. Conceptually a ForeignKey with unique=True constraint is similar to OneToOneField.
#
# So if you want to ensure that every picture has one user and vice-versa use a OneToOneField.
#
# If you want one user to have any number of pictures use a ForeignKey.
#
# The way things are selected are also different. In case of doing OneToOneField, you can do user.picture and get the
# picture directly. In case of ForeignKey you will do user.picture_set[0] to get the first picture or access all the
# pictures associated with that user.
#
# MultiTableInheritance implicitly uses OneToOneField internally and you can see where the concept originated from.

# REFER : https://stackoverflow.com/questions/13115207/differences-between-one-to-one-and-foreign-key-relationships


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	ACTIVE = 'Active'
	DEACTIVATED = 'DeActivated'
	
	ACCOUNT_STATUS = [
		(ACTIVE, 'Active'),
		(DEACTIVATED, 'DeActivated'),
	]
	ALERT_ON = 'On'
	ALERT_OFF = 'Off'
	
	ALERT_STATUS = [
		(ALERT_ON, 'On'),
		(ALERT_OFF, 'Off'),
	]
	
	UserProfilePictureUrl = models.ImageField(upload_to="UserProfilePicture/%Y/%m/%d", default="UserProfilePicture/2020/04/24/DefaultProfileImage.png", blank=True)
	
	phone_regex = RegexValidator(regex=r'^\d{10}$', message="Must be in length of 10")
	UserMobileNumber = models.CharField(validators=[phone_regex], max_length=10, unique=True)  # validators should
	# be a list
	UserAltMobileNumber = models.CharField(validators=[phone_regex], max_length=10, blank=True)
	# validators should be a list
	
	UserCompanyName = models.CharField(max_length=50, blank=False)
	
	year_regex = RegexValidator(regex=r'^\d{4}$', message="Must be in length of 4 and all digits")
	UserCompanyYear = models.CharField(validators=[year_regex], max_length=4, blank=True)
	
	UserAccountStatus = models.CharField(
		max_length=20,
		choices=ACCOUNT_STATUS,
		default=ACTIVE,
	)
	UserAlertStatus = models.CharField(
		max_length=20,
		choices=ALERT_STATUS,
		default=ACTIVE,
	)

	def __str__(self):
		return self.user.username


