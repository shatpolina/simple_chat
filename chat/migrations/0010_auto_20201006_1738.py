# Generated by Django 3.1.1 on 2020-10-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20201006_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confroom',
            name='ID_room',
            field=models.CharField(default='6XWK8F0Q3E', max_length=10, primary_key=True, serialize=False),
        ),
    ]