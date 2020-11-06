# Generated by Django 2.2 on 2020-10-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20201027_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_id', models.CharField(max_length=100)),
                ('suggestion_msg', models.TextField()),
                ('suggestion_date', models.DateField(max_length=8)),
            ],
        ),
        migrations.AlterField(
            model_name='studentleave',
            name='status',
            field=models.CharField(default='Panding_Request', max_length=100),
        ),
    ]
