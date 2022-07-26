# Generated by Django 4.0.6 on 2022-07-19 16:06

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_recipe_recipedateupdated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='RecipePhoto_name',
            field=models.CharField(default=datetime.datetime(2022, 7, 19, 16, 5, 50, 162646, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='UserPhoto_file',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='UserPhoto_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='UserPhoto_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='RecipeDateUpdated',
            field=models.DateField(default=datetime.datetime(2022, 7, 19, 16, 5, 40, 29391, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserDateAdded',
            field=models.DateField(default=datetime.datetime(2022, 7, 19, 16, 5, 40, 69036, tzinfo=utc)),
        ),
    ]
