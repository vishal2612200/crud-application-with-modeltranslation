from modeltranslation.translator import translator, TranslationOptions
from .models import Post, Newpost

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'message',)

class NewpostTranslationOptions(TranslationOptions):
    fields = ('title', 'message',)

translator.register(Post, PostTranslationOptions)
translator.register(Newpost, NewpostTranslationOptions)
