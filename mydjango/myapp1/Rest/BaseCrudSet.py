import pandas as pd
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from myapp1.repository.match import MatchRepository
from myapp1.repository.player import PlayerRepository
from myapp1.repository.team import TeamRepository


class BaseCrudSet(APIView):
    model = None
    serializer_class = None
    unit_of_work = None

    def get_object_by_id(self, pk):
        try:
            return self.unit_of_work.get(pk=pk)
        except self.model.DoesNotExist:
            return None

    def get(self, request, pk=None):
        if pk:
            instance = self.get_object_by_id(pk)
            if not instance:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(instance)
        else:
            instances = self.unit_of_work.all()
            serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        instance = self.get_object_by_id(pk)
        if not instance:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object_by_id(pk)
        if not instance:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AvgAgePerTeamAPIView(APIView):
    def get(self, request):
        data = TeamRepository.get_avg_age_per_team()
        df = pd.DataFrame(data)

        fig = self.create_avg_age_bar_chart(df)

        graph_html = fig.to_html(full_html=False)

        return Response({"graph_html": graph_html})

    def create_avg_age_bar_chart(self, df, px=None):
        fig = px.bar(df, x='team_name', y='avg_age', title='Середній вік по командах')
        return fig

class PlayerCountPerTeamAPIView(APIView):
    def get(self, request):
        data = TeamRepository.get_player_count_per_team()
        df = pd.DataFrame(data)

        mean_count = df['player_count'].mean()
        min_count = df['player_count'].min()
        max_count = df['player_count'].max()
        median_count = df['player_count'].median()

        return Response({
            'mean': mean_count,
            'min': min_count,
            'max': max_count,
            'median': median_count
        })


class TopTeamsByGoalsAPIView(APIView):
    def get(self, request):
        data = TeamRepository.get_top_teams_by_goals()
        df = pd.DataFrame(data)

        mean_goals = df['total_goals'].mean()
        min_goals = df['total_goals'].min()
        max_goals = df['total_goals'].max()
        median_goals = df['total_goals'].median()

        return Response({
            'mean': mean_goals,
            'min': min_goals,
            'max': max_goals,
            'median': median_goals
        })


class HighScoreDifferenceMatchesAPIView(APIView):
    def get(self, request):
        score_difference = request.query_params.get('score_difference', None)

        if score_difference is not None:
            score_difference = int(score_difference)

        data = MatchRepository.get_high_score_difference_matches(score_difference)
        df = pd.DataFrame(data)

        return Response(df.to_dict(orient='records'))


class PlayersAbove30APIView(APIView):
    def get(self, request):
        age = request.query_params.get('age', None)

        if age is not None:
            age = int(age)

        data = PlayerRepository.get_players_above_30(age)
        df = pd.DataFrame(data)

        mean_players = df['count'].mean()
        min_players = df['count'].min()
        max_players = df['count'].max()
        median_players = df['count'].median()

        return Response({
            'mean': mean_players,
            'min': min_players,
            'max': max_players,
            'median': median_players
        })


class MatchCountByMonthAPIView(APIView):
    def get(self, request):
        data = MatchRepository.get_match_count_by_month()
        df = pd.DataFrame(data)

        mean_matches = df['count'].mean()
        min_matches = df['count'].min()
        max_matches = df['count'].max()
        median_matches = df['count'].median()

        return Response({
            'mean': mean_matches,
            'min': min_matches,
            'max': max_matches,
            'median': median_matches
        })


