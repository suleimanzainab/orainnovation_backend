# Generated by Django 4.2.5 on 2024-01-12 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ora_innovation_app', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ora_innovation_app.activities'),
        ),
    ]