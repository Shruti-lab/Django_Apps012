# Generated by Django 4.2.6 on 2023-12-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_rename_name_menu_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='age',
            field=models.IntegerField(default=45),
            preserve_default=False,
        ),
    ]
