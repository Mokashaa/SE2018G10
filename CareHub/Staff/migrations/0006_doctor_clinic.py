# Generated by Django 2.1.2 on 2019-02-06 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clinics', '0002_auto_20190206_1656'),
        ('Staff', '0005_auto_20190206_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='clinic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Clinics.Service'),
        ),
    ]
