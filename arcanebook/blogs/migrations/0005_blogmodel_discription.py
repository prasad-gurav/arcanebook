# Generated by Django 4.1 on 2022-08-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blogmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='discription',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]