# Generated by Django 4.2.5 on 2023-09-28 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Linkapp', '0010_companydata_employeedetail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetail1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=255)),
                ('e_head', models.TextField()),
                ('e_link', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='EmployeeDetail',
        ),
        migrations.RenameModel(
            old_name='CompanyData',
            new_name='CompanyData1',
        ),
        migrations.AddField(
            model_name='employeedetail1',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='Linkapp.companydata1'),
        ),
    ]
