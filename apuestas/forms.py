
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

        temp = {}
        temp['pais'] = response["competitions"][i]["area"]["name"]
        temp['liga'] = response["competitions"][i]["name"]
        temp['id'] = response["competitions"][i]["id"]

        datos.append(response["competitions"][i]["name"])
        print(datos)

    #return render(request,'index.html', {'seasons': datos[0]})
    return datos

class BetsForm(forms.ModelForm):

    class Meta:
        model = Bets

        #fields = '__all__'

       #CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)

        fields = [
            'local_team',
            'visiting_team',
            'league',
            'balance',
		]

        """labels = {
			'user_id' : 'id de usuario',
            'local_team' : 'equipo local',
            'visiting_team': 'equipo visitante',
            'league' : 'liga',
            'balance': 'valor apuesta',
            'date': 'fecha',
            'bets_state' : 'estado apuesta' ,
		}"""

class WinBetsForm(forms.ModelForm):
    class Meta:
        model = WinBets

        fields = '__all__'

        """fields = {
            'bets_id',
            'team_bet',
        }

        labels = {
            'bets_id' : 'id de apuesta',
            'team_bet' : 'equipo ganador',
        }"""

class MarkerBetsForm(forms.ModelForm):
    class Meta:
        model = MarkerBets

        fields = '__all__'

        """fields = {
            'bets_id',
            'local_marker',
            'visiting_marker',
        }

        labels = {
            'bets_id' : 'id de apuesta',
            'local_marker' : 'marcador local',
            'visiting_marker': 'marcador visitante',
        }"""

class GoalsBetsForm(forms.ModelForm):
    class Meta:
        model = GoalsBets

        fields = '__all__'

        """fields = {
            'bets_id',
            'goals_dif',
        }

        labels = {
            'bets_id' : 'id de apuesta',
            'goals_dif' : 'diferencia de goles',
        }"""