# Generated by Django 4.2.7 on 2023-11-29 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shared_count', models.PositiveIntegerField(default=0)),
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feed_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
