# Generated by Django 3.1.7 on 2021-03-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20210302_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество'),
        ),
    ]
