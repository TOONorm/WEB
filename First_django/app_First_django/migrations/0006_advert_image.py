# Generated by Django 4.2.3 on 2023-08-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_First_django', '0005_remove_advert_update_at_advert_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='image',
            field=models.ImageField(default='', upload_to='First_django/', verbose_name='изображение'),
            preserve_default=False,
        ),
    ]