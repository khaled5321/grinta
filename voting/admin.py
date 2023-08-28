from django.contrib import admin
from .models import Vote, Competition, Singer


admin.site.register(Vote)
admin.site.register(Competition)
admin.site.register(Singer)