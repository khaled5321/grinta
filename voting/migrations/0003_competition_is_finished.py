# Generated by Django 4.2.4 on 2023-08-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voting", "0002_competition_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="competition",
            name="is_finished",
            field=models.BooleanField(default=False),
        ),
    ]
