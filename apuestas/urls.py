from django.urls import path
from apuestas import views

urlpatterns = [
    path ('',views.get_ligas),
    path('d/<int:id>',views.get_aquipos),
    #path('bet/<int:id>', views.bets_view, name='index'),
    ]