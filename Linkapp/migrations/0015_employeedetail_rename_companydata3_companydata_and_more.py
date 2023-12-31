# Generated by Django 4.2.5 on 2023-09-28 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Linkapp', '0014_companydata3_employeedetail3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=255)),
                ('e_head', models.TextField()),
                ('e_link', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='CompanyData3',
            new_name='CompanyData',
        ),
        migrations.DeleteModel(
            name='EmployeeDetail3',
        ),
        migrations.AddField(
            model_name='employeedetail',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Linkapp.companydata'),
        ),
    ]
