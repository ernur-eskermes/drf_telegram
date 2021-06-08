from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from tg_bot.models import Message, Chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'message',
            'created',
        )

    def validate(self, attrs):
        chat = Chat.objects.filter(
            user=self.context['request'].user
        ).first()
        if not chat:
            raise ValidationError('Вы не создали чат.')
        if not chat.chat_id:
            raise ValidationError('Вы не авторизовались в telegram. '
                                  'Отправьте свой токен боту, '
                                  'чтобы авторизоватся.')
        return attrs

    def create(self, validated_data):
        instance = Message.objects.create(
            message=validated_data['message'],
            chat=Chat.objects.get(user=self.context['request'].user)
        )
        return instance


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            'id',
            'token'
        )

    def create(self, validated_data):
        instance, _ = Chat.objects.get_or_create(
            user=self.context['request'].user
        )
        return instance
