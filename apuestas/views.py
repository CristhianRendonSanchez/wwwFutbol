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
	return datos


def bets_view(request):
	if request.method == 'POST':
		form = ApuestaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('ganador') #aqui redirecciono a ala seleccion de tipo de apuesta
	else:
		form = ApuestaForm()
	return render(request, 'index.html', {'form':form})

def bets_win_view(request):
	if request.method == 'POST':
		form = Apuestas_por_ganador(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index') #aqui redirecciono ala pagina principal de apuestas
	else:
		form = Apuestas_por_ganador()
	return render(request, 'index.html', {'form':form})

def bets_Marker_view(request):
	if request.method == 'POST':
		form = Apuestas_por_marcador(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index') #aqui redirecciono ala pagina principal de apuestas
	else:
		form = Apuestas_por_marcador()
	return render(request, 'index.html', {'form':form})


def bets_goals_view(request):
	if request.method == 'POST':
		form = Apuestas_por_dif_goles(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index') #aqui redirecciono ala pagina principal de apuestas
	else:
		form = Apuestas_por_dif_goles()
	return render(request, 'index.html', {'form':form})

