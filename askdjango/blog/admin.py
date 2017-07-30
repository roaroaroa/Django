#blog/admin.py
from django.contrib import admin
from .models import Post
from .models import Check

from blog.models import Rice_E
from blog.models import Rice_L
from blog.models import Water_E
from blog.models import Water_L
from blog.models import Tissue_E
from blog.models import Tissue_L

from blog.models import Comment
from blog.models import Board

admin.site.register(Post)
admin.site.register(Check)






admin.site.register(Rice_E)
admin.site.register(Rice_L)
admin.site.register(Water_E)
admin.site.register(Water_L)
admin.site.register(Tissue_E)
admin.site.register(Tissue_L)

admin.site.register(Comment)
admin.site.register(Board)
