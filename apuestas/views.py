import json
import http.client

from django.shortcuts import render, redirect
import requests

# Create your views here.
from apuestas.forms import *


def get_ligas(request):
	connection = http.client.HTTPConnection('api.football-data.org')
	headers = {'X-Auth-Token':
				   '81e49a62695c431f83675e9f9da4e078'}
	connection.request('GET', '/v2/competitions?areas=2049', None, headers)
	response = json.loads(connection.getresponse().read().decode())

	# datos = response.json()

	datos = []

	for i in range(0, response["count"]):
		temp = {}
		temp['pais'] = response["competitions"][i]["area"]["name"]
		temp['liga'] = response["competitions"][i]["name"]
		temp['id'] = response["competitions"][i]["id"]
		datos.append(temp)
		print(datos[i])

	#return render(request,'index.html', {'seasons': datos[0]})
	return render(request ,"apuestas.html", {'ligas': datos})

def get_aquipos(request,id):
	connection = http.client.HTTPConnection('api.football-data.org')
	headers = {'X-Auth-Token':
				   '81e49a62695c431f83675e9f9da4e078'}
	connection.request('GET', '/v2/competitions?id=2045', None, headers)
	response = json.loads(connection.getresponse().read().decode())
	print(response)

"""
def bets_view(request,id):
	user = UserProfile.objects.get(id=id)
	balance = user.balance
	form = BetsForm(request.POST)
	if form.is_valid():
		if balance < form.cleaned_data['balance']:
			pay = form.cleaned_data['balance'] - balance
			dateB = datetime.now()
			bet = Bets(user_id = id,
						local_team= form.cleaned_data['local_team'],
						visiting_team=form.cleaned_data['visiting_team'],
						league=form.cleaned_data['league'],
						balance= form.cleaned_data['balance'],
						date = dateB,
						bets_state= True)
			#form.save()
			bet.save()
		return redirect('index') #aqui redirecciono a ala seleccion de tipo de apuesta


def bets_win_view(request):
	if request.method == 'POST':
		form = WinBetsForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index') #aqui redirecciono ala pagina principal de apuestas
	else:
		form = WinBetsForm()
	return render(request, 'apuestas.html', {'form':form})

def bets_Marker_view(request):
	if request.method == 'POST':
		form = MarkerBetsForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index') #aqui redirecciono ala pagina principal de apuestas
	else:
		form = MarkerBetsForm()
	return render(request, 'apuestas.html', {'form':form})


def bets_goals_view(request):
	if request.method == 'POST':
		form = GoalsBetsForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index') #aqui redirecciono ala pagina principal de apuestas
	else:
		form = GoalsBetsForm()
	return render(request, 'index.html', {'form':form})"""

