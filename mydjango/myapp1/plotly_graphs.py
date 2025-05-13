import plotly.express as px
import pandas as pd

def create_avg_age_bar_chart(data):
    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x='team_name',
        y='avg_age',
        title='Середній вік по командах'
    )

    fig.update_layout(
        xaxis={'categoryorder': 'total descending'}
    )

    return fig

def create_match_count_line_chart(data):
    df = pd.DataFrame(data)

    fig = px.pie(
        df,
        names='month',
        values='count',
        title='Розподіл кількості матчів по місяцях'
    )

    return fig

def create_top_teams_by_goals_chart(data):
    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x='team_name',
        y='total_goals',
        title='Топ команди за кількістю голів'
    )

    fig.update_layout(
        xaxis_title='Команди',
        yaxis_title='Забиті голи',
        xaxis={'categoryorder': 'total descending'}
    )

    return fig

def create_player_count_chart(data):
    df = pd.DataFrame(data)

    fig = px.pie(
        df,
        names='team_name',
        values='player_count',
        title="Кількість гравців у команді",
        labels={'team_name': 'Team Name', 'player_count': 'Player Count'}
    )

    return fig

def create_high_score_difference_chart(data):
    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x='team_name',
        y='home_match_count',
        labels={'team_name': 'Команда', 'home_match_count': 'Кількість матчів'},
        title='Кількість матчів у кожній команді'
    )

    fig.update_layout(
        xaxis={'categoryorder': 'total descending'}
    )

    return fig

def create_players_chart(data):
    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x='team__team_name',
        y='count',
        title='Кількість гравців за заданим віком',
        labels={'count': 'Кількість'}
    )

    fig.update_layout(
        xaxis={'categoryorder': 'total descending'}
    )

    return fig
