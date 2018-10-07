# Generated by Django 2.1.1 on 2018-09-29 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_distribution_centre_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution_centre_Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Xcoordinate', models.FloatField(default=0)),
                ('Ycoordinate', models.FloatField(default=0)),
                ('DC_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Distribution_centre')),
            ],
        ),
    ]
