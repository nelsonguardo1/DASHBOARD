# Generated by Django 4.0.4 on 2022-11-06 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tornado', '0006_alter_tornado_tncategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tornado',
            name='tncategoria',
        ),
    ]
