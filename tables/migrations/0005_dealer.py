# Generated by Django 2.1.1 on 2018-09-29 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_distribution_centre_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('DL_ID', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('Contact', models.IntegerField(default=0)),
                ('DC_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Distribution_centre')),
            ],
        ),
    ]
