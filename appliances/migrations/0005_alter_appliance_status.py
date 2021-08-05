# Generated by Django 3.2.5 on 2021-08-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0004_alter_appliance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliance',
            name='status',
            field=models.IntegerField(choices=[(0, 'Company registered'), (10, 'To apply'), (20, 'Contacted by company'), (30, 'First meet incoming'), (40, 'Technical test'), (50, 'In progress'), (60, 'Offer received'), (70, 'Aborted'), (80, 'Refused by company')], default=0),
        ),
    ]
