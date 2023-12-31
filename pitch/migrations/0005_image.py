# Generated by Django 4.2.4 on 2023-08-27 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pitch', '0004_remove_pitch_pitch_images_delete_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pitch_images/')),
                ('pitch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitch.pitch')),
            ],
        ),
    ]
