# Generated by Django 4.2.18 on 2025-01-31 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_review_comment_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(related_name='books', to='app1.genre'),
        ),
    ]
