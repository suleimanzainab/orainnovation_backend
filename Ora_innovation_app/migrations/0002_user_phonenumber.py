# Generated by Django 4.2.5 on 2024-01-10 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ora_innovation_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]