from django.db import models

class CrmStatus(models.Model):

    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    class Meta:
        verbose_name = ("Статус")
        verbose_name_plural = ("Статусы")

    def __str__(self):
        return self.status_name

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата')
    order_name = models.CharField(max_length=255, verbose_name='Имя')
    order_phone = models.CharField(max_length=255, verbose_name='Телефон')
    order_status = models.ForeignKey(CrmStatus, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')
    
    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

class CrmComment(models.Model):
    comment = models.ForeignKey(Order, verbose_name=("Заявка"), on_delete=models.CASCADE)
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    
    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    
 