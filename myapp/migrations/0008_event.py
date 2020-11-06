# Generated by Django 2.2 on 2020-10-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remaining_fees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_nm', models.CharField(max_length=100)),
                ('event_date', models.CharField(max_length=100)),
                ('event_time', models.CharField(max_length=100)),
                ('status', models.CharField(default='active', max_length=100)),
            ],
        ),
    ]