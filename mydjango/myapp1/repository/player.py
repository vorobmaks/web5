from django.db.models import Count
from myapp1.models import Player
from myapp1.repository.basic import BaseRepository

class PlayerRepository(BaseRepository):
    model = Player

    @staticmethod
    def get_players_above_30(age=None):
        query = Player.objects
        if age is not None:
            query = query.filter(age=age)
        return query.values('team__team_name').annotate(count=Count('id'))
