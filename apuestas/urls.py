from django.urls import path
from apuestas import views

urlpatterns = [
    path ('liga/<int:user_id>',views.get_ligas, name ='ligas'),
    path('team/<int:id>/<int:user_id>',views.get_partidos, name= 'team'),
    path('bet/<int:id>/<int:user_id>', views.bets_view, name='bet'),
    path('bets/<int:id>', views.bets_view, name='bets'),
    path('save', views.save_bet, name='save'),
    path('win/<int:id>', views.bets_win_view, name='win'),
    path('marker/<int:id>', views.bets_Marker_view, name='marker'),
    path('goal/<int:id>', views.bets_goals_view, name='goal'),
    path('myBets/<int:id>', views.list_bets, name='mybets'),
    ]