from django.contrib import admin
from rango.models import Category, Tip, UserProfile, Season, Outfit, List, Item

# Registering the models.
class TipsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'content', 'likes')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class OutfitsAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'username')

class SeasonsAdmin(admin.ModelAdmin):
    list_display = ('name', 'maxtemp', 'mintemp')

class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'slug')
    
    prepopulated_fields = {'slug':('name',)}

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('list', 'title','completed')

# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tip, TipsAdmin)
admin.site.register(Season, SeasonsAdmin)
admin.site.register(Outfit, OutfitsAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Item, ItemsAdmin)
admin.site.register(UserProfile)