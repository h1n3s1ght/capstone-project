# Generated by Django 4.0.6 on 2022-07-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('RecipeId', models.AutoField(primary_key=True, serialize=False)),
                ('RecipeName', models.CharField(max_length=100)),
                ('RecipeMeal', models.CharField(max_length=30)),
                ('RecipePhoto_file', models.ImageField(upload_to='images')),
                ('RecipePhoto_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserFName', models.CharField(max_length=30)),
                ('UserLName', models.CharField(max_length=30)),
            ],
        ),
    ]
