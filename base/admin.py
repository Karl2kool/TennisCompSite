from django.contrib import admin

from .models  import Fillin, Score, Match


# Register your models here.
admin.site.register(Fillin)
admin.site.register(Score)
admin.site.register(Match)