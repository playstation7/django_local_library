# Generated by Django 3.2.1 on 2021-05-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0009_alter_visit_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]