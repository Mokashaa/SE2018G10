# Generated by Django 2.1.2 on 2019-02-13 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinics', '0028_auto_20190212_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('a', 'Clinic'), ('b', 'Scan')], max_length=7),
        ),
    ]