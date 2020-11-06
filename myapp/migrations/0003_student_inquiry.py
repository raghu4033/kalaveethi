# Generated by Django 2.2 on 2020-10-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=8)),
                ('fname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='', max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=8)),
                ('address', models.TextField()),
                ('education', models.CharField(max_length=100)),
                ('course', models.CharField(choices=[('fashion', 'fashion'), ('graphics', 'graphics'), ('fineart', 'fineart'), ('textile', 'textile'), ('jwellery', 'jwellery')], default='', max_length=200)),
                ('reference', models.CharField(max_length=100)),
            ],
        ),
    ]