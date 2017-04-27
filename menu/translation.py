from modeltranslation.translator import translator, TranslationOptions
from menu.models import MenuItem

class MenuTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(MenuItem, MenuTranslationOptions)
