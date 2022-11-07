# Generated by Django 4.0.4 on 2022-11-06 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etv', '0009_auto_20190430_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='earthquake',
            name='country',
        ),
        migrations.RemoveField(
            model_name='earthquake',
            name='date',
        ),
        migrations.RemoveField(
            model_name='earthquake',
            name='intensity',
        ),
        migrations.RemoveField(
            model_name='earthquake',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='earthquake',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='earthquake',
            name='place',
        ),
        migrations.AddField(
            model_name='earthquake',
            name='año1',
            field=models.CharField(default='2019', max_length=50),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='año2',
            field=models.CharField(default='2020', max_length=50),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='año3',
            field=models.CharField(default='2021', max_length=50),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='categoria',
            field=models.CharField(default='Muertes Violentas', max_length=50),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='cifra1',
            field=models.CharField(default='383', max_length=50),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='cifra2',
            field=models.CharField(default='427', max_length=50),
        ),
        migrations.AddField(
            model_name='earthquake',
            name='cifra3',
            field=models.CharField(default='462', max_length=50),
        ),
    ]