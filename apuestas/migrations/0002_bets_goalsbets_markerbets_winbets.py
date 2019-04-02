# Generated by Django 2.2 on 2019-04-02 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_team', models.CharField(max_length=255)),
                ('visiting_team', models.CharField(max_length=255)),
                ('league', models.CharField(max_length=255)),
                ('balance', models.IntegerField(default=0)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('bets_state', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WinBets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_bet', models.CharField(max_length=255)),
                ('bets_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuestas.Bets')),
            ],
        ),
        migrations.CreateModel(
            name='MarkerBets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_marker', models.IntegerField(default=0)),
                ('visiting_marker', models.IntegerField(default=0)),
                ('bets_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuestas.Bets')),
            ],
        ),
        migrations.CreateModel(
            name='GoalsBets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_dif', models.IntegerField(default=0)),
                ('bets_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuestas.Bets')),
            ],
        ),
    ]
