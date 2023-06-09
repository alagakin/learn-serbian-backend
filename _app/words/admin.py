from django.contrib import admin

from topics.models import Topic
from words.models import Word, Translation, Text, TextTranslation


class TranslationInlineAdmin(admin.TabularInline):
    model = Translation
    extra = 3


class TextTranslationInlineAdmin(admin.TabularInline):
    model = TextTranslation
    extra = 2


class TopicsOfTheWordInlineAdmin(admin.TabularInline):
    model = Topic.words.through
    extra = 2


class WordAdmin(admin.ModelAdmin):
    list_display = ['title', 'part', 'texts_count', 's3_id']
    inlines = [TranslationInlineAdmin, TopicsOfTheWordInlineAdmin]


class TranslationAdmin(admin.ModelAdmin):
    list_display = ['title', 'lang', 'word']


class TextAdmin(admin.ModelAdmin):
    list_display = ['content', 'words_count', 'translations_count', 'get_words']
    readonly_fields = ['words_count', 'get_words']

    def get_words(self, obj):
        return ", ".join(obj.words.values_list('title', flat=True))

    get_words.short_description = 'Words'

    inlines = [TextTranslationInlineAdmin]


class TextTranslationAdmin(admin.ModelAdmin):
    list_display = ['id', 'preview', 'text', 'lang', 'words_count', 'get_words']
    readonly_fields = ['words_count', 'get_words']

    def get_words(self, obj):
        return ", ".join(obj.text.words.values_list('title', flat=True))

    get_words.short_description = 'Words'


admin.site.register(Word, WordAdmin)
admin.site.register(Translation, TranslationAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(TextTranslation, TextTranslationAdmin)
