from bokeh.palettes import Spectral11
from bokeh.plotting import figure
from math import pi
from bokeh.transform import cumsum
from bokeh.palettes import Category20c
import pandas as pd

def create_avg_age_bar_chart_bokeh(data):
    df = pd.DataFrame(data)
    df = df.sort_values(by='avg_age', ascending=False)

    team_names = df['team_name'].tolist()
    avg_ages = df['avg_age'].tolist()

    p = figure(
        x_range=team_names,
        height=350,
        title="Середній вік по командах",
        toolbar_location=None,
        tools=""
    )
    p.vbar(
        x=team_names,
        top=avg_ages,
        width=0.8,
        color="navy"
    )
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.axis_label = "Команди"
    p.yaxis.axis_label = "Середній вік"

    return p

def create_match_count_bar_chart_bokeh(data):
    df = pd.DataFrame(data)

    if len(df) == 0:
        raise ValueError("DataFrame is empty. No data to display.")

    num_colors = len(df)
    if num_colors in Category20c:
        colors = Category20c[num_colors]
    else:
        colors = Category20c[20][:num_colors]

    df['angle'] = df['count'] / df['count'].sum() * 2 * pi
    df['color'] = colors

    p = figure(
        height=350,
        title="Кількість матчів за місяць",
        toolbar_location=None,
        tools="hover",
        tooltips="@month: @count",
        x_range=(-0.5, 1.0)
    )

    p.wedge(
        x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='month', source=df
    )

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    return p

def create_top_teams_by_goals_chart_bokeh(data):
    df = pd.DataFrame(data)

    team_names = df['team_name'].tolist()
    total_goals = df['total_goals'].tolist()

    p = figure(
        x_range=team_names,
        height=350,
        title="Топ команди за кількістю забитих м'ячів",
        toolbar_location=None,
        tools=""
    )
    p.vbar(x=team_names, top=total_goals, width=0.8, color="orange")
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = "vertical"
    p.xaxis.axis_label = "Команди"
    p.yaxis.axis_label = "Кількість голів"

    return p

def create_player_count_chart_bokeh(data):
    df = pd.DataFrame(data)

    df['angle'] = df['player_count'] / df['player_count'].sum() * 2 * pi
    df['color'] = Category20c[len(df)]

    p = figure(
        height=350,
        title="Кількість гравців у командах",
        toolbar_location=None,
        tools="hover",
        tooltips="@team_name: @player_count",
        x_range=(-0.5, 1.0)
    )

    p.wedge(
        x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='team_name', source=df
    )

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    return p

def create_players_chart_bokeh(data):
    df = pd.DataFrame(data)
    df = df.sort_values(by='count', ascending=False)

    team_names = df['team__team_name'].tolist()
    player_counts = df['count'].tolist()

    p = figure(
        x_range=team_names,
        height=350,
        title="Кількість гравців за віком",
        toolbar_location=None,
        tools=""
    )
    p.vbar(
        x=team_names,
        top=player_counts,
        width=0.8,
        color="purple"
    )
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = "vertical"
    p.xaxis.axis_label = "Команди"
    p.yaxis.axis_label = "Кількість гравців"

    return p

def create_team_match_counts_chart_bokeh(data):
    df = pd.DataFrame(data)

    df = df.sort_values(by='home_match_count', ascending=False)

    team_names = df['team_name'].tolist()
    match_counts = df['home_match_count'].tolist()

    p = figure(
        x_range=team_names,
        height=350,
        title="Кількість матчів у кожній команді",
        toolbar_location=None,
        tools=""
    )
    p.vbar(
        x=team_names,
        top=match_counts,
        width=0.8,
        color=Spectral11[:len(team_names)]
    )
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.axis_label = "Команди"
    p.yaxis.axis_label = "Кількість матчів"
    p.xaxis.major_label_orientation = 1

    return p