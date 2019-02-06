# Generated by Django 2.1.2 on 2019-02-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('availability', models.BooleanField(default=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('appointments', models.PositiveSmallIntegerField()),
                ('type', models.CharField(max_length=1)),
                ('doctor', models.ManyToManyField(to='Staff.Doctor')),
            ],
        ),
    ]
