# Generated by Django 2.2 on 2020-10-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_auto_20201030_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
