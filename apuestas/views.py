import json
import http.client

from django.shortcuts import render
import requests

# Create your views here.
def inicio(request):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token':
                   '81e49a62695c431f83675e9f9da4e078'}
    connection.request('GET', '/v2/competitions/', None, headers)
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

    return render(request,'index.html', {'seasons': datos[10]})
