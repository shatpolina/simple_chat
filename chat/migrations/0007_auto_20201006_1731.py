# Generated by Django 3.1.1 on 2020-10-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20201006_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='ID_user',
            field=models.UUIDField(default=0, editable=False, primary_key=True, serialize=False),
        ),
    ]