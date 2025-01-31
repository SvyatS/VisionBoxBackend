# Generated by Django 3.2.12 on 2022-08-18 07:01

from django.db import migrations, models
import users.utils


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.UUIDField(default=users.utils.id_generator, editable=False, primary_key=True, serialize=False, verbose_name="Project's code"),
        ),
    ]
