from django.contrib import admin
from search.models import Searchtitles

# Register your models here.
class SearchtitlesAdmin(admin.ModelAdmin):
    list_display=['title']


admin.site.register(Searchtitles, SearchtitlesAdmin)