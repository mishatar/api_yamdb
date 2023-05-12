from django.contrib import admin

from .models import Categories, Comment, Genres, Review, Title

admin.site.register(Categories)
admin.site.register(Genres)
admin.site.register(Title)
admin.site.register(Comment)
admin.site.register(Review)
