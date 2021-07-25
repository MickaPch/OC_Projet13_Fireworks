# Generated by Django 3.2.5 on 2021-07-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_rename_contacts_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='company',
            name='adress1',
            field=models.TextField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='zipcode',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]
