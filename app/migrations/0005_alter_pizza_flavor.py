# Generated by Django 3.2 on 2024-06-23 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20240622_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='flavor',
            field=models.CharField(choices=[('MARG', 'Margarita'), ('PEPP', 'Pepperoni'), ('HAWA', 'Hawaiana')], max_length=10),
        ),
    ]