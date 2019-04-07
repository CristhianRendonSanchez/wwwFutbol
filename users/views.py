from django.shortcuts import render, redirect
from apuestas.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from users.forms import UserForm


def show(request):
    return render(request, "index.html")


def user_logout(request):
    logout(request)
    return render(request, 'index.html')


def register(request):
    print("Holiii, estyo entrando al métodooo!!!!")
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            #Esto es para que envie a la página de login user a lo que registre
            return render(request, "loginUser.html")
            #NOTA: Esto no debe ser render sino redirect, como en el metodo de login
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'registration.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        print(password)

        user = authenticate(email=email, password=password)

        if user:
            if user.is_active:
                superuser = user.is_superuser
                print(superuser)
                login(request, user)
                if superuser:
                    request.session['email'] = email
                    return redirect('index')
                else:
                    request.session['email'] = email
                    return render(request, 'league.html', {'user_id': user.id})
                    #El vigi debe cambiar esto al name que le haya pueesto a su url inicial
                    #tipo: return redirect('lamadredelvigi', user_id: user.id)
            return HttpResponse("Tu cuenta está inactiva")

        else:
            print("Alguien intentó entrar y falló")
            print("Username: {} and password:{}".format(email, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'index.html', {})