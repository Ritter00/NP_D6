# Generated by Django 3.2.6 on 2021-09-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
