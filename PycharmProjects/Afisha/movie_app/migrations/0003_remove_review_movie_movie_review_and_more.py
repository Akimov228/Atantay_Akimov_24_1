# Generated by Django 4.1.7 on 2023-02-19 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_review_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='review',
            field=models.ManyToManyField(blank=True, to='movie_app.review'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.director'),
        ),
    ]
