# Generated by Django 2.2.6 on 2019-10-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20191020_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='descrption',
            field=models.TextField(max_length=100, null=True, verbose_name='unit_descrption'),
        ),
    ]
