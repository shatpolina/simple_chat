# Generated by Django 3.1.1 on 2020-10-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0036_auto_20201009_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confroom',
            name='ID_room',
            field=models.CharField(default='33DJKPBBAX', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='ID_user',
            field=models.CharField(editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]