# Generated by Django 4.1 on 2022-10-25 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitur_autentikasi', '0004_alter_profile_telephone_alter_profile_whatsapp'),
        ('crowdfunding', '0002_alter_crowdfund_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='crowdfund',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fitur_autentikasi.profile'),
        ),
    ]
