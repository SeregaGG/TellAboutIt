# Generated by Django 4.0.3 on 2022-04-25 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TAIApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]