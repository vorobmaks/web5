from bokeh.embed import components
from django.http import JsonResponse
from django.shortcuts import render

from myapp1.bokeh_graphs import create_avg_age_bar_chart_bokeh, \
    create_top_teams_by_goals_chart_bokeh, create_player_count_chart_bokeh, create_players_chart_bokeh, \
    create_match_count_bar_chart_bokeh, create_team_match_counts_chart_bokeh
from myapp1.plotly_graphs import create_match_count_line_chart, create_top_teams_by_goals_chart, \
    create_player_count_chart, create_avg_age_bar_chart, create_high_score_difference_chart, \
    create_players_chart
from myapp1.repository.context import Context

def dashboard_home(request):
    return render(request, 'zaputu.html')

context = Context()

def dashboard_view(request):
    data = context.team.get_avg_age_per_team()

    fig = create_avg_age_bar_chart(data)

    graph_html = fig.to_html(full_html=False)

    return render(request, 'dashboard.html', {'graph_html': graph_html})

def dash1(request):
    data = context.match.get_match_count_by_month()

    fig = create_match_count_line_chart(data)

    graph_html = fig.to_html(full_html=False)

    return render(request, 'dash1.html', {'graph_html': graph_html})

def dash2(request):
    data = context.team.get_top_teams_by_goals()

    fig = create_top_teams_by_goals_chart(data)
    graph_div = fig.to_html(full_html=False)

    return render(request, 'dash2.html', {'graph_div': graph_div})

def dash3(request):
    data = context.team.get_player_count_per_team()

    fig = create_player_count_chart(data)

    graph_div = fig.to_html(full_html=False)

    return render(request, 'dash3.html', {'graph_div': graph_div})

def dash4(request):
    score_difference = request.GET.get('score_difference', 3)
    data = context.match.get_high_score_difference_matches(score_difference=score_difference)

    fig = create_high_score_difference_chart(data)

    graph_div = fig.to_html(full_html=False)

    return render(request, 'dash4.html', {'graph_div': graph_div})

def dash5(request):
    age = request.GET.get('age', 30)
    data = context.player.get_players_above_30(age=age)

    fig = create_players_chart(data)

    graph_div = fig.to_html(full_html=False)

    return render(request, 'dash5.html', {'graph_div': graph_div})

def filter_data(request):
    dashboard = request.GET.get('dashboard', None)
    graph_library = request.GET.get('graph_library', 'bokeh')

    if graph_library == 'bokeh':
        if dashboard == 'bokeh1':
            data = context.team.get_avg_age_per_team()
            fig = create_avg_age_bar_chart_bokeh(data)
        elif dashboard == 'bokeh2':
            data = context.match.get_match_count_by_month()
            fig = create_match_count_bar_chart_bokeh(data)
        elif dashboard == 'bokeh3':
            data = context.team.get_top_teams_by_goals()
            fig = create_top_teams_by_goals_chart_bokeh(data)
        elif dashboard == 'bokeh4':
            data = context.team.get_player_count_per_team()
            fig = create_player_count_chart_bokeh(data)
        elif dashboard == 'bokeh5':
            data = context.team.get_team_match_counts()
            fig = create_team_match_counts_chart_bokeh(data)
        elif dashboard == 'bokeh6':
            age = request.GET.get('age', 30)
            data = context.player.get_players_above_30(age=age)
            fig = create_players_chart_bokeh(data)
        else:
            return JsonResponse({'error': 'Invalid dashboard type'})

        script, div = components(fig)
        return JsonResponse({'script': script, 'div': div})

    else:
        if dashboard == 'dashboard':
            data = context.team.get_avg_age_per_team()
            fig = create_avg_age_bar_chart(data)
        elif dashboard == 'dash1':
            data = context.match.get_match_count_by_month()
            fig = create_match_count_line_chart(data)
        elif dashboard == 'dash2':
            data = context.team.get_top_teams_by_goals()
            fig = create_top_teams_by_goals_chart(data)
        elif dashboard == 'dash3':
            data = context.team.get_player_count_per_team()
            fig = create_player_count_chart(data)
        elif dashboard == 'dash4':
            data = context.team.get_team_match_counts()
            fig = create_high_score_difference_chart(data)
        elif dashboard == 'dash5':
            age = request.GET.get('age', 30)
            data = context.player.get_players_above_30(age=age)
            fig = create_players_chart(data)
        else:
            return JsonResponse({'error': 'Invalid dashboard type'})

        graph_html = fig.to_html(full_html=False)

        return JsonResponse({'graph_html': graph_html})


def bokeh1(request):
    data = context.team.get_avg_age_per_team()
    p = create_avg_age_bar_chart_bokeh(data)
    script, div = components(p)

    return render(request, 'bokeh1.html', {'script': script, 'div': div})

def bokeh2(request):
    data = context.team.get_player_count_per_team()
    p =  create_player_count_chart_bokeh(data)

    script, div = components(p)

    return render(request, 'bokeh2.html', {'script': script, 'div': div})

def bokeh3(request):
    data = context.match.get_match_count_by_month()

    p = create_match_count_bar_chart_bokeh(data)

    script, div = components(p)

    return render(request, 'bokeh3.html', {'script': script, 'div': div})

def bokeh4(request):
    data = context.player.get_players_above_30()
    p =  create_players_chart_bokeh(data)

    script, div = components(p)

    return render(request, 'bokeh4.html', {'script': script, 'div': div})

def bokeh6(request):
    data = context.team.get_top_teams_by_goals()

    p = create_top_teams_by_goals_chart_bokeh(data)

    script, div = components(p)

    return render(request, 'bokeh6.html', {'script': script, 'div': div})

def bokeh5(request):
    data = context.match.get_high_score_difference_matches()
    p =  create_team_match_counts_chart_bokeh(data)

    script, div = components(p)

    return render(request, 'bokeh5.html', {'script': script, 'div': div})