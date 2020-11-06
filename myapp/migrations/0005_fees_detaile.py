# Generated by Django 2.2 on 2020-10-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_student_reg_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='fees_detaile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_id', models.CharField(max_length=100)),
                ('installment_no', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('payment_date', models.DateField(max_length=8)),
                ('payment_type', models.CharField(max_length=100)),
                ('recipt_no', models.CharField(max_length=100)),
            ],
        ),
    ]