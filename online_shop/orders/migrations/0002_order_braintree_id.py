# Generated by Django 3.0.6 on 2020-05-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="braintree_id",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]