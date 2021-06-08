from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Message(models.Model):
    message = models.TextField(
        'Message'
    )
    created = models.DateTimeField(
        'Created',
        auto_now_add=True
    )
    chat = models.ForeignKey(
        'Chat',
        on_delete=models.CASCADE,
        verbose_name='Chat',
        related_name='messages'
    )

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class Chat(models.Model):
    token = models.CharField(
        'Token',
        help_text='Token for authentication in chat. '
                  'Leave it blank to generate automatically',
        max_length=255,
        blank=True
    )
    chat_id = models.CharField(
        'Chat ID',
        max_length=100,
        blank=True
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )

    def save(self, *args, **kwargs):
        if self.token == '':
            self.token = str(uuid4())
        super(Chat, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'


@receiver(post_save, sender=Message)
def send_message_to_telegram(sender, instance, *args, **kwargs):
    from .management.commands.bot import bot
    if kwargs['created']:
        if not instance.chat.chat_id:
            return
        text = '{}, я получил от тебя сообщение:\n{}'.format(
            instance.chat.user.username,
            instance.message,
        )
        bot.send_message(
            instance.chat.chat_id,
            text
        )
