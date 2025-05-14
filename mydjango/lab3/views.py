from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
import requests


url = 'http://127.0.0.1:8000/api/teams/'

def team_list(request):
    response = requests.get(url)
    if response.status_code == 200:
        teams = response.json()
    else:
        teams = []
    return render(request, 'team_list.html', {'teams': teams})

def team_detail(request, pk):
    response = requests.get(url + str(pk))
    if response.status_code == 200:
        team = response.json()
    else:
        team = None
    return render(request, 'team_detail.html', {'team': team})


def team_form(request, pk=None):
    if pk:
        response = requests.get(url + str(pk))
        if response.status_code == 200:
            team = response.json()
        else:
            team = None
    else:
        team = None

    if request.method == 'POST':
        data = {
            'team_name': request.POST.get('name'),
            'city': request.POST.get('city'),
            'stadium': request.POST.get('stadium'),
        }
        if team:
            response = requests.put(url + f'{pk}/', json=data)
        else:

            response = requests.post(url, json=data)

        if response.status_code in [200, 201]:
            return redirect('team-list')

    return render(request, 'team_form.html', {'team': team})


def team_delete(request, pk):
    if request.method == 'POST':
        response = requests.delete(url + str(pk))
        if response.status_code == 204:
            return redirect('team-list')

    return HttpResponseForbidden("Forbidden: Invalid request method.")

def spa_view(request):
    return render(request, 'index.html')
