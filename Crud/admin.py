from django.contrib import admin
from django.conf import settings
from modeltranslation.admin import TranslationAdmin
from .models import Post #add this to import the Post model


class PostAdmin(TranslationAdmin):
    group_fieldsets = True


admin.site.register(Post, PostAdmin) #add this to register the Post model
if not settings.DEBUG:
    admin.site.unregister(Post)

