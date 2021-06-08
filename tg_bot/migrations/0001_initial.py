# Generated by Django 3.2.4 on 2021-06-08 16:03

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
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, help_text='Token for authentication in chat. Leave it blank to generate automatically', max_length=255, verbose_name='Token')),
                ('chat_id', models.CharField(blank=True, max_length=100, verbose_name='Chat ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='tg_bot.chat', verbose_name='Chat')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
