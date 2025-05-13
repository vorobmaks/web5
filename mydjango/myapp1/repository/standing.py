from myapp1.models import Standing
from myapp1.repository.basic import BaseRepository


class StandingRepository(BaseRepository):
    model = Standing