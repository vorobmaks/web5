from myapp1.models import Statistic
from myapp1.repository.basic import BaseRepository


class StatisticRepository(BaseRepository):
    model = Statistic