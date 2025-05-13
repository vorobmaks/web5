from django.db.models import Count, F
from django.db.models.functions import Abs

from myapp1.models import Match
from myapp1.repository.basic import BaseRepository


class MatchRepository(BaseRepository):
    model = Match

    @staticmethod
    def get_high_score_difference_matches(score_difference=None):
        query = Match.objects
        if score_difference is not None:
            query = query.annotate(
                score_difference=Abs(F('score_home') - F('score_away'))
            ).filter(score_difference__gt=score_difference)
        return query.values('team1__team_name', 'team2__team_name', 'score_home', 'score_away', 'date')

    @staticmethod
    def get_match_count_by_month():
        return Match.objects.annotate(month=F('date__month')).values('month').annotate(count=Count('id')).order_by(
            'month')
