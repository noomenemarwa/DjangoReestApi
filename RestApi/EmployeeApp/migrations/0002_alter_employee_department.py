# Generated by Django 4.1.2 on 2022-10-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Department',
            field=models.CharField(max_length=500),
        ),
    ]