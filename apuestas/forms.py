
import json
import http.client
from datetime import datetime

from django import forms


from apuestas.models import *


def get_ligas():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token':
                   '81e49a62695c431f83675e9f9da4e078'}
    connection.request('GET', '/v2/competitions?areas=2049', None, headers)
    response = json.loads(connection.getresponse().read().decode())

    # datos = response.json()

    datos = []

    for i in range(0, response["count"]):
        """
        temp = {}
        temp['pais'] = response["competitions"][i]["area"]["name"]
        temp['liga'] = response["competitions"][i]["name"]
        temp['id'] = response["competitions"][i]["id"]
        """
        datos.append(response["competitions"][i]["name"])
        print(datos)

    #return render(request,'index.html', {'seasons': datos[0]})
    return datos

class ApuestaForm(forms.ModelForm):

    class Meta:
        model = Bets

        league = forms.ChoiceField(choices=get_ligas())
        date = forms.DateTimeField(initial=datetime.now())

        fields = [
            'user_id',
            'local_team',
            'visiting_team',
            'league',
            'balance',
            'date',
            'bets_state' ,
		]

        labels = {
			'user_id' : 'id de usuario',
            'local_team' : 'equipo local',
            'visiting_team': 'equipo visitante',
            'league' : 'liga',
            'balance': 'valor apuesta',
            'date': 'fecha',
            'bets_state' : 'estado apuesta' ,
		}

class Apuestas_por_ganador(forms.ModelForm):
    class Meta:
        model = WinBets

        fields = {
            'bets_id',
            'team_bet',
        }

        labels = {
            'bets_id' : 'id de apuesta',
            'team_bet' : 'equipo ganador',
        }

class Apuestas_por_marcador(forms.ModelForm):
    class Meta:
        model = MarkerBets

        fields = {
            'bets_id',
            'local_marker',
            'visiting_marker',
        }

        labels = {
            'bets_id' : 'id de apuesta',
            'local_marker' : 'marcador local',
            'visiting_marker': 'marcador visitante',
        }

class Apuestas_por_dif_goles(forms.ModelForm):
    class Meta:
        model = GoalsBets

        fields = {
            'bets_id',
            'goals_dif',
        }

        labels = {
            'bets_id' : 'id de apuesta',
            'goals_dif' : 'diferencia de goles',
        }