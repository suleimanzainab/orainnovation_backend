# Generated by Django 4.2.5 on 2024-01-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Ora_innovation_app", "0009_orders_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="deleveryDateTime",
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name="orders",
            name="pickupDateTime",
            field=models.CharField(),
        ),
    ]