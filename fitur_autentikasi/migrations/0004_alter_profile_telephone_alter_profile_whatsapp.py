# Generated by Django 4.1 on 2022-10-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitur_autentikasi', '0003_alter_profile_line_alter_profile_poin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telephone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='whatsapp',
            field=models.CharField(max_length=15),
        ),
    ]
