from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


# создание и настройка разных БД с помощью ORM


class Advert(models.Model):
    title = models.CharField('Название', max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Укажите, возможен ли торг')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('изображение', upload_to='First_django/')

    @admin.display(description='дата создания')
    def created_date(self):
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green"; font: bold>Сегодня в {}</span>', created_time
            )
        return self.create_at.strftime('%d.%m.%Y')

    @admin.display(description='дата обновления')
    def update_at(self):
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: yellow"; font: bold>Сегодня в {}</span>', created_time
            )
        return self.create_at.strftime('%d.%m.%Y')

    @admin.display(description='изображение')
    def get_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-heigh: 80px;">', url=self.image.url
            )

    def __str__(self):
        return (f"Advertisment: (id={self.id}, title={self.title}, price-{self.price}")

    class Meta:
        db_table = 'advertisments'
