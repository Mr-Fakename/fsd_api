# Generated by Django 4.1.6 on 2023-03-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_image_delete_blogpostimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='summary',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
