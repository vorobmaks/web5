from django.contrib import admin

from myapp1.models import Team, Player, Match, Standing, Result, Manager, Statistic

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Standing)
admin.site.register(Result)
admin.site.register(Manager)
admin.site.register(Statistic)
