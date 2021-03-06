# Generated by Django 2.2 on 2020-10-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_delete_studentleave'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_id', models.CharField(max_length=100)),
                ('sname', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('leavedate', models.DateField(max_length=8)),
                ('Leave_catagory', models.CharField(choices=[('Sick_Leave', 'Sick_Leave'), ('Extended_Sick', 'Extended_Sick'), ('Emergency_Leave', 'Emergency_Leave'), ('Long_Leave', 'Long_Leave')], default='', max_length=200)),
                ('leave_reason', models.CharField(max_length=100)),
                ('leave_day', models.CharField(max_length=100)),
                ('status', models.CharField(default='deactive', max_length=100)),
            ],
        ),
    ]
