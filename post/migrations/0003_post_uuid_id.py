# Generated by Django 4.2.4 on 2023-08-27 17:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_image_alter_follow_id_alter_likes_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uuid_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
