from django.contrib import admin
from .models import Advert


# настройки отображения в панели админ


class ArvertAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','auction','created_date', 'update_at', 'user','get_image']
    list_filter = ['price','auction','create_at']
    actions = ['make_auction_as_true',"make_auction_as_false"]
    fieldsets = (
        ('Общие', {
            'fields':('title','description', 'user','image')
        }),
        ('Финансы',{
            'fields':('price','auction'),
            'classes':['collapse']
        })
    )

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self,reqest,queryset):
        queryset.update(auction=True)

    @admin.action(description='Удалить возможность торга')
    def make_auction_as_false(self, reqest, queryset):
        queryset.update(auction=False)

admin.site.register(Advert,ArvertAdmin)