# Generated by Django 4.2.5 on 2023-09-28 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Linkapp', '0013_employeedetail2_rename_companydata1_companydata2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyData3',
            fields=[
                ('comp_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('website', models.URLField(max_length=250)),
                ('industry', models.TextField()),
                ('company_size', models.TextField()),
                ('headquarter', models.TextField()),
                ('founded', models.CharField(max_length=255)),
                ('foll', models.CharField(max_length=255)),
                ('specialties', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetail3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compy_name', models.CharField(max_length=255)),
                ('e_name', models.CharField(max_length=255)),
                ('e_head', models.TextField()),
                ('e_link', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Linkapp.companydata3')),
            ],
        ),
        migrations.RemoveField(
            model_name='employeedetail2',
            name='company',
        ),
        migrations.DeleteModel(
            name='CompanyData2',
        ),
        migrations.DeleteModel(
            name='EmployeeDetail2',
        ),
    ]