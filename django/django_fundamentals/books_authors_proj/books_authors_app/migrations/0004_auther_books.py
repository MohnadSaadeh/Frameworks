# Generated by Django 5.0.3 on 2024-04-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_auther_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='auther',
            name='books',
            field=models.ManyToManyField(related_name='authers', to='books_authors_app.book'),
        ),
    ]
