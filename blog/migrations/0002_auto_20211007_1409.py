# Generated by Django 3.2.7 on 2021-10-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('slug',)},
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]