# Generated by Django 5.1.3 on 2024-12-05 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trash_classify', '0006_hisdata_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hisdata',
            name='created_by',
        ),
    ]
