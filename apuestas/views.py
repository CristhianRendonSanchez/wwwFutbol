import json
import http.client

from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
import requests


def index(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        nombres_usuarios = data.get("name_user")
        contraseña_usuarios = data.get("password_user")
        print(nombres_usuarios)
        print(contraseña_usuarios)
    var = {
        "form_login": form,
    }
    return render(request, "index.html", var)


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

    return render(request, 'index.html', {'seasons': datos[10]})
