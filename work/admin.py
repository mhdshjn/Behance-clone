from django.contrib import admin
from .models import Work
from .models import Tag
from .models import Comment
from .models import Appreciate
from .models import Tools

admin.site.register(Work)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Appreciate)
admin.site.register(Tools)
