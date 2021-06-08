from django.db import models


class Message(models.Model):
    message = models.TextField(
        'Message'
    )
    created = models.DateTimeField(
        'Created',
        auto_now_add=True
    )

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
