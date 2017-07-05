#blog/admin.py
from django.contrib import admin
from .models import Post
from .models import Scrapping
from .models import Emart
admin.site.register(Post)

admin.site.register(Scrapping)

admin.site.register(Emart)
