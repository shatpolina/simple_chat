# Generated by Django 3.1.1 on 2020-10-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0024_auto_20201006_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confroom',
            name='ID_room',
            field=models.CharField(default='9K9N17CYMZ', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='ID_user',
            field=models.CharField(default='99bac363-b123-4d21-b052-bcac2d6f777e', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]