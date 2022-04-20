# Generated by Django 4.0.3 on 2022-04-18 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_rename_blood_group_group_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_form', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.blood'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]