from django.db.models import Sum, Count, Avg

from myapp1.models import Team
from myapp1.repository.basic import BaseRepository


class TeamRepository(BaseRepository):
    model = Team
    @staticmethod
    def get_avg_age_per_team():
        return Team.objects.annotate(avg_age=Avg('player__age')).values('team_name', 'avg_age')

    @staticmethod
    def get_player_count_per_team():
        return Team.objects.annotate(player_count=Count('player')).values('team_name', 'player_count')

    @staticmethod
    def get_top_teams_by_goals():
        return Team.objects.annotate(
            total_goals=Sum('home_matches__score_home') + Sum('away_matches__score_away')
        ).order_by('-total_goals').values('team_name', 'total_goals')

    @staticmethod
    def get_team_match_counts():
        return Team.objects.annotate(home_match_count=Count('home_matches') + Count('away_matches')) \
            .values('team_name', 'home_match_count')

