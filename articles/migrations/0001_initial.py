# Generated by Django 3.1.7 on 2021-02-27 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('type', models.CharField(choices=[('PH', 'Phone'), ('GA', 'Gadget'), ('AC', 'Acsessories')], default='GA', max_length=2)),
                ('slug', models.SlugField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('text', models.CharField(blank=True, max_length=255, verbose_name='Текст статьи')),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('gadget', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='articles.item')),
            ],
        ),
    ]
