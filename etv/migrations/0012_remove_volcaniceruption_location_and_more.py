# Generated by Django 4.0.4 on 2022-11-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etv', '0011_rename_año1_earthquake_taño1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volcaniceruption',
            name='location',
        ),
        migrations.RemoveField(
            model_name='volcaniceruption',
            name='mountain',
        ),
        migrations.RemoveField(
            model_name='volcaniceruption',
            name='spread_area',
        ),
        migrations.RemoveField(
            model_name='volcaniceruption',
            name='subtype',
        ),
        migrations.RemoveField(
            model_name='volcaniceruption',
            name='type',
        ),
        migrations.RemoveField(
            model_name='volcaniceruption',
            name='year',
        ),
        migrations.AddField(
            model_name='volcaniceruption',
            name='año1',
            field=models.CharField(default='2019', max_length=50),
        ),
        migrations.AddField(
            model_name='volcaniceruption',
            name='año2',
            field=models.CharField(default='2020', max_length=50),
        ),
        migrations.AddField(
            model_name='volcaniceruption',
            name='año3',
            field=models.CharField(default='2021', max_length=50),
        ),
        migrations.AddField(
            model_name='volcaniceruption',
            name='categoria',
            field=models.CharField(default='Suicidios', max_length=50),
        ),
        migrations.AddField(
            model_name='volcaniceruption',
            name='cifra1',
            field=models.CharField(default='42', max_length=50),
        ),
        migrations.AddField(
            model_name='volcaniceruption',
            name='cifra2',
            field=models.CharField(default='37', max_length=50),
        ),
        migrations.AddField(
            model_name='volcaniceruption',
            name='cifra3',
            field=models.CharField(default='26', max_length=50),
        ),
        migrations.AlterField(
            model_name='tsunami',
            name='tcifra1',
            field=models.CharField(default='197', max_length=50),
        ),
        migrations.AlterField(
            model_name='tsunami',
            name='tcifra2',
            field=models.CharField(default='223', max_length=50),
        ),
        migrations.AlterField(
            model_name='tsunami',
            name='tcifra3',
            field=models.CharField(default='246', max_length=50),
        ),
    ]