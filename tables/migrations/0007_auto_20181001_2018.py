# Generated by Django 2.1.1 on 2018-10-01 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_dealer_address_ship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='DC_ID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tables.Distribution_centre'),
        ),
    ]