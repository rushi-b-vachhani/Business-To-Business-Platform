# Generated by Django 3.0.1 on 2020-04-23 22:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerAccountApp', '0003_selleraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='BusinessCardBackUrl',
            field=models.ImageField(blank=True, default='DefaultBusinessCardImage.png', upload_to='BusinessCardBackPicture/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='business',
            name='BusinessCardFrontUrl',
            field=models.ImageField(blank=True, default='DefaultBusinessCardImage.png', upload_to='BusinessCardFrontPicture/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='SellerAltFaxNumber',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Must be in length of 15', regex='^\\d{15}$')]),
        ),
        migrations.AlterField(
            model_name='seller',
            name='SellerFaxNumber',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Must be in length of 15', regex='^\\d{15}$')]),
        ),
        migrations.AlterField(
            model_name='seller',
            name='SellerPromoterCEOName',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
