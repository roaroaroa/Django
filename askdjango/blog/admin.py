#blog/admin.py
from django.contrib import admin
from .models import Post
from .models import Scrapping
from .models import Emart
from .models import Handling
from .models import Discount

admin.site.register(Post)

admin.site.register(Scrapping)


class PostAdmin(admin.ModelAdmin):
    list_display=['id','title', 'price']

admin.site.register(Emart, PostAdmin)

admin.site.register(Handling)

admin.site.register(Discount)