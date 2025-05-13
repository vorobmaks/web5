from myapp1.models import TeamMatch
from myapp1.repository.basic import BaseRepository


class TeamMatchRepository(BaseRepository):
    model = TeamMatch