#blog/admin.py
from django.contrib import admin
from .models import Post
from .models import Check
from .models import Scrapping
from .models import Emart
from .models import Handling
from .models import Handling2
from .models import Handling3
from .models import Discount
from blog.models import Rice_E
from blog.models import Rice_L
from blog.models import Water_E
from blog.models import Water_L
from blog.models import Tissue_E
from blog.models import Tissue_L

admin.site.register(Post)
admin.site.register(Check)

admin.site.register(Scrapping)


class PostAdmin(admin.ModelAdmin):
    list_display=['id','title', 'price']

admin.site.register(Emart, PostAdmin)

admin.site.register(Handling)

admin.site.register(Handling2)

admin.site.register(Handling3)

admin.site.register(Discount)


admin.site.register(Rice_E)
admin.site.register(Rice_L)
admin.site.register(Water_E)
admin.site.register(Water_L)
admin.site.register(Tissue_E)
admin.site.register(Tissue_L)
