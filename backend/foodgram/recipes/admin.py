from django.contrib.admin import ModelAdmin, TabularInline, register
from django.utils.safestring import mark_safe

from .models import AmountIngredient, Ingredient, Recipe, Tag


class IngredientInline(TabularInline):
    model = AmountIngredient
    extra = 2


@register(AmountIngredient)
class LinksAdmin(ModelAdmin):
    pass


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = (
        'name', 'measurement_unit',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )

    save_on_top = True
    empty_value_display = 'Значение не указано'


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = (
        'name', 'author', 'get_image',
    )
    fields = (
        ('name', 'cooking_time',),
        ('author', 'tags',),
        ('text',),
        ('image',),
    )
    raw_id_fields = ('author',)
    search_fields = (
        'name', 'author',
    )
    list_filter = (
        'name', 'author__username',
    )

    inlines = (IngredientInline,)
    save_on_top = True
    empty_value_display = 'Значение не указано'

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" hieght="30"')

    get_image.short_description = 'Изображение'


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = (
        'name', 'color', 'slug',
    )
    search_fields = (
        'name', 'color'
    )

    save_on_top = True
    empty_value_display = 'Значение не указано'
