# Generated by Django 4.2.15 on 2024-08-13 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='average_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='author',
            name='fans_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='author',
            name='ratings_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='author',
            name='text_reviews_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='author',
            name='works_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(default='unknown', max_length=10),
        ),
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
