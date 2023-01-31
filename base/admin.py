from django.contrib import admin

from .models  import Fillin, Score, Match, Team,Week


# Register your models here.
admin.site.register(Fillin)
admin.site.register(Score)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Week)