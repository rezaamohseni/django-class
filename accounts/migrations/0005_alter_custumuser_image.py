# Generated by Django 4.2 on 2024-07-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_custumuser_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="custumuser",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="user"),
        ),
    ]
