from myapp1.models import Season
from myapp1.repository.basic import BaseRepository


class SeasonRepository(BaseRepository):
    model = Season