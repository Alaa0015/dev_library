from django.contrib import admin

# Register your models here.

from tech_library.models import Developer, Topic, Theme

admin.site.register(Developer)
admin.site.register(Theme)
admin.site.register(Topic)