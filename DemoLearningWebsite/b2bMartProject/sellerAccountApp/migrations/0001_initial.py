# Generated by Django 3.0.1 on 2020-04-02 08:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountsApp', '0003_auto_20200402_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SellerPromoterCEOName', models.CharField(max_length=30)),
                ('SellerFaxNumber', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Must be in length of 15', regex='^\\d{15}$')])),
                ('SellerAltFaxNumber', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Must be in length of 15', regex='^\\d{15}$')])),
                ('Profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accountsApp.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Statutory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StatutoryGSTIN', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Must be in length of 15', regex='^\\d{15}]$')])),
                ('StatutoryPanNumber', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Must be in length of 10', regex='^\\d{10}]$')])),
                ('StatutoryTanNumber', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Must be in length of 10', regex='^\\d{10}]$')])),
                ('StatutoryCinNumber', models.CharField(blank=True, max_length=21, validators=[django.core.validators.RegexValidator(message='Must be in length of 21', regex='^\\d{21}]$')])),
                ('StatutoryDgftNumber', models.CharField(blank=True, max_length=21, validators=[django.core.validators.RegexValidator(message='Must be in length of 6', regex='^\\d{15}]$')])),
                ('Seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sellerAccountApp.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BusinessCeoName', models.CharField(blank=True, max_length=30)),
                ('BusinessBusinessType', models.CharField(blank=True, max_length=30)),
                ('BusinessOwnershipType', models.CharField(blank=True, max_length=30)),
                ('BusinessNumberOfEmployee', models.CharField(blank=True, max_length=6, validators=[django.core.validators.RegexValidator(message='Must be in length of 6', regex='^\\d{0-6}$')])),
                ('BusinessAnnualTurnover', models.CharField(blank=True, max_length=30, validators=[django.core.validators.RegexValidator(message='Must be in length of 10', regex='^\\d{0-10}$')])),
                ('BusinessCompanyLogo', models.ImageField(blank=True, default='DefaultCompanyLogoImage.png', upload_to='CompanyLogoPicture/%Y/%m/%d')),
                ('BusinessCompanyWebsite', models.CharField(blank=True, max_length=100)),
                ('BusinessCatalogUrl', models.CharField(blank=True, max_length=100)),
                ('BusinessCardFrontUrl', models.CharField(blank=True, max_length=100)),
                ('BusinessCardBackUrl', models.ImageField(blank=True, default='DefaultBusinessCardImage.png', upload_to='BusinessCardPicture/%Y/%m/%d')),
                ('Seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sellerAccountApp.Seller')),
            ],
        ),
    ]
