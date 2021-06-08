import telebot
from django.conf import settings
from django.core.management.base import BaseCommand
from tg_bot.models import Chat

bot = telebot.TeleBot(settings.TG_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    text = 'Привет!\nНапишите мне токен, который ' \
           'вы сгенерировали в своем личном кабинете'
    bot.send_message(
        message.chat.id,
        text
    )


@bot.message_handler(content_types=['text'])
def auth_by_token(message):
    chat = Chat.objects.filter(
        token=message.text
    ).first()
    if not chat:
        bot.send_message(
            message.chat.id,
            'Неправильный токен!',
        )
        return
    if chat.chat_id:
        bot.send_message(
            message.chat.id,
            'Вы уже авторизованы',
        )
        return
    chat.chat_id = message.chat.id
    chat.save()

    bot.send_message(
        message.chat.id,
        'Вы успешно авторизованы!',
    )


class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        bot.polling()
