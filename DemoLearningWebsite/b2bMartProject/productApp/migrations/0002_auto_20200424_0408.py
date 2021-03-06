# Generated by Django 3.0.1 on 2020-04-23 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProductCode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductDeliveryTime',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductDescription',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductImageUrl',
            field=models.ImageField(blank=True, default='DefaultProductPicture.png', null=True, upload_to='ProductPicture/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductMinimumOrderQuantity',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductPackagingDetails',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductProductionCapacity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
