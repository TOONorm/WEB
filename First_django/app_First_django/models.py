from django.db import models

class Advert(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField('Название', max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField('Цена', max_digits=10, decimal_places=3)
    auction = models.BooleanField('Торг', help_text='Укажите, возможен ли торг')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return (f"{self.app_label}(id={self.ID}, title={self.title}, price-{self.price}")
