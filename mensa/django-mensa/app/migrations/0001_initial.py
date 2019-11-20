# Generated by Django 2.1.7 on 2019-05-07 16:36

import app.models
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d', models.CharField(choices=[(app.models.WeekDay('Monday'), 'Monday'), (app.models.WeekDay('Tuesday'), 'Tuesday'), (app.models.WeekDay('Wednesday'), 'Wednesday'), (app.models.WeekDay('Thursday'), 'Thursday'), (app.models.WeekDay('Friday'), 'Friday'), (app.models.WeekDay('Saturday'), 'Saturday'), (app.models.WeekDay('Sunday'), 'Sunday')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Day')),
            ],
        ),
        migrations.CreateModel(
            name='Plates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_menu', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[(app.models.MenuChoice('Primo'), 'Primo'), (app.models.MenuChoice('Secondo'), 'Secondo'), (app.models.MenuChoice('Contorno'), 'Contorno'), (app.models.MenuChoice('Dessert'), 'Dessert')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='plates',
            name='menu_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Service'),
        ),
        migrations.AddField(
            model_name='employee',
            name='plate_chosen',
            field=models.ManyToManyField(to='app.Plates'),
        ),
    ]