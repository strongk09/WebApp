from django.contrib import admin
from blog.models import Post, Storage_Location, Item, RSO


class ItemAdmin(admin.ModelAdmin):
    list_display = ('Tag_num', 'Item_name', 'Manf_name', 'Seller_name', 'Pur_date', 'Pur_price')
    search_fields = ['Item_name']

class Storage_LocationAdmin(admin.ModelAdmin):
    list_display = ('Store_local', 'Store_add', 'Store_room')
    search_fields = ['Store_room']

admin.site.register(Post)
admin.site.register(Storage_Location, Storage_LocationAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(RSO)
