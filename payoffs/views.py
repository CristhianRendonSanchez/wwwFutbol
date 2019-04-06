from django.shortcuts import render, redirect
from users.forms import UserPayoffForm
from apuestas.models import Payoffs
from apuestas.models import UserProfile
from datetime import datetime


def show(request):
    users = UserProfile.objects.filter(is_superuser=0, is_active=1)
    return render(request, "admin.html", {'users':  users})


def edit(request, id):
    user = UserProfile.objects.get(id=id)
    return render(request, 'edit.html', {'user': user})


def update(request, id):
    user = UserProfile.objects.get(id=id)
    balance = user.balance
    form = UserPayoffForm(request.POST, instance=user)
    if form.is_valid():
        consigned = form.cleaned_data['balance'] - balance
        date = datetime.now()
        payoff = Payoffs(consigned_amount=consigned, date_amount=date, user_id_id=user.id)
        form.save()
        payoff.save()
    return redirect('index')


def delete(request, id):
    user = UserProfile.objects.get(id=id)
    user.is_active = 0
    user.save()
    return redirect('index')



