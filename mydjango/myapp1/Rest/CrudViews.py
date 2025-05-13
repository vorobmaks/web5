from myapp1.repository.context import Context
from myapp1.Rest.serializer import PlayerSerializer,TeamSerializer,MatchSerializer
from myapp1.Rest.BaseCrudSet import BaseCrudSet
from myapp1.models import Player, Team, Match

context = Context()

class PlayerCrudView(BaseCrudSet):
    model = Player
    serializer_class = PlayerSerializer
    unit_of_work = context.player

class TeamCrudView(BaseCrudSet):
    model = Team
    serializer_class = TeamSerializer
    unit_of_work = context.team

class MatchCrudView(BaseCrudSet):
    model = Match
    serializer_class = MatchSerializer
    unit_of_work = context.match


