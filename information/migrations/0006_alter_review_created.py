# Generated by Django 4.1.2 on 2022-11-02 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0005_alter_review_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 2, 20, 56, 57, 596522)),
        ),
    ]