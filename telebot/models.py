from django.db import models

class TeleSettings(models.Model):
    tg_token  = models.CharField(verbose_name="Токен", max_length=200)
    tg_chat  = models.CharField(verbose_name="ID чата", max_length=200)
    tg_message = models.TextField(verbose_name='Текст сообщения')
    

    class Meta:
        verbose_name = ("Настройку")
        verbose_name_plural = ("Настройки")

    def __str__(self):
        return self.tg_chat

