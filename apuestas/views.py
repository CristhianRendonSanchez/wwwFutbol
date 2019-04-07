import json
import http.client

from django.shortcuts import render, redirect
import requests

# Create your views here.
from apuestas.forms import *


def get_ligas(request):
	connection = http.client.HTTPConnection('api.football-data.org')
	headers = {'X-Auth-Token':'81e49a62695c431f83675e9f9da4e078'}
	connection.request('GET', '/v2/competitions', None, headers)
	response = json.loads(connection.getresponse().read().decode())

	# datos = response.json()

	datos = []

	for i in range(0, response["count"]):
		temp = {}
		if response["competitions"][i]["plan"] == "TIER_ONE":
			temp['pais'] = response["competitions"][i]["area"]["name"]
			temp['liga'] = response["competitions"][i]["name"]
			temp['id'] = response["competitions"][i]["id"]
			temp['code'] = response["competitions"][i]["code"]
			print(response["competitions"][i]["id"])
			datos.append(temp)

	#return render(request,'index.html', {'seasons': datos[0]})
	return render(request ,"league.html", {'ligas': datos})

def get_partidos(request,id):
	connection = http.client.HTTPConnection('api.football-data.org')
	headers = {'X-Auth-Token':'81e49a62695c431f83675e9f9da4e078'}
	connection.request('GET', '/v2/competitions/' + str(id) + '/matches?status=SCHEDULED', None, headers)
	response = json.loads(connection.getresponse().read().decode())

	datos = []
	for i in range(0, response["count"]):
		temp = {}
		temp['id'] = response["matches"][i]["id"]
		temp['date'] = response["matches"][i]["utcDate"]
		#temp['status'] = response["matches"][i]["status"]
		temp['local_team'] = response["matches"][i]["homeTeam"]["name"]
		#temp['local_team_id'] = response["matches"][i]["homeTeam"]["id"]
		temp['visisting_team'] = response["matches"][i]["awayTeam"]["name"]
		#temp['visisting_team_id'] = response["matches"][i]["awayTeam"]["id"]
		print(temp)
		datos.append(temp)


	return render(request, "match.html", {'teams': datos, 'liga': response["competition"]["name"]})



def consultar_partidos(id):
	connection = http.client.HTTPConnection('api.football-data.org')
	headers = {'X-Auth-Token': '81e49a62695c431f83675e9f9da4e078'}
	connection.request('GET', '/v2/matches/' + str(id), None, headers)
	response = json.loads(connection.getresponse().read().decode())

	datos = {}
	datos['liga'] = response["match"]["competition"]["name"]
	datos['date'] = response["match"]["utcDate"]
	datos['status'] = response["match"]["status"]
	datos['score_local'] = response["match"]["score"]["fullTime"]["homeTeam"]
	datos['score_visiting'] = response["match"]["score"]["fullTime"]["awayTeam"]
	datos['local_team'] = response["match"]["homeTeam"]["name"]
	datos['visisting_team'] = response["match"]["awayTeam"]["name"]

	return datos

def bets_view(request, id):
	partido = consultar_partidos(id)
	return  render(request, "bet.html", {'match' : partido})






""""
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
	return render(request, 'league.html', {'form':form})

def bets_Marker_view(request):
	if request.method == 'POST':
		form = MarkerBetsForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index') #aqui redirecciono ala pagina principal de apuestas
	else:
		form = MarkerBetsForm()
	return render(request, 'league.html', {'form':form})


def bets_goals_view(request):
	if request.method == 'POST':
		form = GoalsBetsForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index') #aqui redirecciono ala pagina principal de apuestas
	else:
		form = GoalsBetsForm()
	return render(request, 'index.html', {'form':form})"""

