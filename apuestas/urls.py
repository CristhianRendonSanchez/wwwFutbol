from django.urls import path
from apuestas import views

urlpatterns = [
    path ('',views.get_ligas),
    path('team/<int:id>',views.get_partidos, name= 'team'),
    path('bet/<int:id>', views.bets_view, name='bet'),
    ]