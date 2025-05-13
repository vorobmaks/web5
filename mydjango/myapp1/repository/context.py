from myapp1.repository.manager import ManagerRepository
from myapp1.repository.match import MatchRepository
from myapp1.repository.player import PlayerRepository
from myapp1.repository.result import ResultRepository
from myapp1.repository.role import RoleRepository
from myapp1.repository.season import SeasonRepository
from myapp1.repository.standing import StandingRepository
from myapp1.repository.statistic import StatisticRepository
from myapp1.repository.team import TeamRepository
from myapp1.repository.teammatch import TeamMatchRepository


class Context:
    def __init__(self):
        self.manager = ManagerRepository()
        self.match = MatchRepository()
        self.player = PlayerRepository()
        self.result = ResultRepository()
        self.role = RoleRepository()
        self.season = SeasonRepository()
        self.standing = StandingRepository()
        self.team = TeamRepository()
        self.statistic = StatisticRepository()
        self.teammatch = TeamMatchRepository()
