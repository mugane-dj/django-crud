# Generated by Django 4.0.3 on 2022-04-19 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0007_delete_payroll'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
