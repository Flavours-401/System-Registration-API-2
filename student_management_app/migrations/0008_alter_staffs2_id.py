# Generated by Django 4.0 on 2022-01-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0007_staffs2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffs2',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
