# Generated by Django 3.2 on 2024-06-22 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_pizza_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
