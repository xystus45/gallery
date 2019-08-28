# Generated by Django 2.2 on 2019-08-28 13:11

from django.db import migrations
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default=django.utils.timezone.now, upload_to='avatars'),
            preserve_default=False,
        ),
    ]
