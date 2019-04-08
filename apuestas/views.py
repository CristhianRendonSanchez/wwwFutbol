import json
import http.client

from django.shortcuts import render, redirect
import requests

# Create your views here.
from apuestas.forms import *


def get_ligas(request,user_id):
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
	return render(request ,"league.html", {'ligas': datos , 'user':user_id})

def get_partidos(request,id, user_id):
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


	return render(request, "match.html", {'teams': datos, 'liga': response["competition"]["name"] , 'user':user_id})



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

	return datos,id

def bets_view(request, id, user_id):
	partido = consultar_partidos(id)
	return  render(request, "bet.html", {'match' : partido[0], 'id' : partido[1], 'user' : user_id,})


def save_bet(request):
	print(".... entro ....")
	print(request.POST['user_id'])
	user = UserProfile.objects.get(id=request.POST['user_id'])
	print(request.POST['user_id'])
	date = datetime.now()
	bet = Bets(user_id_id= user.id,
			   local_team=request.POST['local_team'],
			   visiting_team=request.POST['visiting_team'],
			   id_match=request.POST['id_match'],
			   league=request.POST['league'],
			   balance=request.POST['balance'],
			   date=date,
			   bets_state=request.POST['bets_state'])
	bet.save()
	print(bet.id)
	datos ={}
	datos['user_id'] = bet.user_id_id
	datos['local_team'] = bet.local_team
	datos['visiting_team'] = bet.visiting_team
	datos['id'] = bet.id
	print("save")
	print(bet.user_id_id)

	return render(request, 'bets.html', {'apuestas': datos})


def bets_win_view(request,id):
	print(id)
	bet = Bets.objects.get(id=id)
	print("winbet")
	print(bet.id)
	print(request.POST['team_bet'])

	winBet = WinBets( bets_id_id = bet.id,
					 team_bet = request.POST['team_bet'])
	winBet.save()

	datos = {}
	datos['user_id'] = bet.user_id_id
	datos['local_team'] = bet.local_team
	datos['visiting_team'] = bet.visiting_team
	datos['id'] = bet.id

	return render(request, 'bets.html', {'apuestas': datos})

def bets_Marker_view(request,id):
	print(id)
	bet = Bets.objects.get(id=id)

	markerBet = MarkerBets(bets_id_id = bet.id,
						   local_marker = request.POST['local_marker'],
						   visiting_marker = request.POST['visiting_marker'])
	markerBet.save()

	datos = {}
	datos['user_id'] = bet.user_id_id
	datos['local_team'] = bet.local_team
	datos['visiting_team'] = bet.visiting_team
	datos['id'] = bet.id
	return render(request, 'bets.html', {'apuestas': datos})


def bets_goals_view(request,id):
	print(id)
	bet = Bets.objects.get(id=id)

	goalBet = GoalsBets(bets_id_id = bet.id,
						goals_dif = request.POST['goals_dif'])
	goalBet.save()

	datos = {}
	datos['user_id'] = bet.user_id_id
	datos['local_team'] = bet.local_team
	datos['visiting_team'] = bet.visiting_team
	datos['id'] = bet.id
	return render(request, 'bets.html', {'apuestas': datos})


