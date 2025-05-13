from myapp1.models import Result
from myapp1.repository.basic import BaseRepository


class ResultRepository(BaseRepository):
    model = Result