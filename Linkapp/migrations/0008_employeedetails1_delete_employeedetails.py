# Generated by Django 4.2.5 on 2023-09-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Linkapp', '0007_employeedetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=255)),
                ('e_head', models.TextField()),
                ('e_link', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='EmployeeDetails',
        ),
    ]
