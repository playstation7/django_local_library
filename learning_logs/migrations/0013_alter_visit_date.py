# Generated by Django 3.2.1 on 2021-05-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0012_auto_20210529_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]