import requests
import os
from statistics import mean
import json

api_key = os.getenv('API_KEY')

players = {
    "alex": "80034246",
    "dan": "77947110",
    "elly": "91301985",
    "justin": "121774797",
    "kellen": "60514922",
}


def get_dota_mmr(user_id):
    name = user_id.lower()
    if name in players:
        r = requests.get(f'https://api.opendota.com/api/players/{players[name]}').json()
        data = r['mmr_estimate']
        return f"Your Estimated MMR is : {str(data['estimate'])}"
    else:
        return "Invalid Response. Type $commands for help."


def get_win_loss_record(user_id):
    name = user_id.lower()
    if name in players:
        r = requests.get(f'https://api.opendota.com/api/players/{players[name]}/wl').json()
        win = r['win']
        loss = r['lose']
        total_games = win + loss
        return f"Out of {total_games} games played: \n" \
               f"WINS: {win} / LOSSES: {loss}"
    else:
        return 'Invalid Response. Type $commands for help.'


def get_player_averages(player_id):
    name = player_id.lower()
    if name in players:
        r = requests.get(f' https://api.opendota.com/api/players/{players[name]}'
                         f'/recentMatches?api_key={api_key}').json()
        kills = [r[0]['kills'], r[1]['kills'], r[2]['kills'], r[3]['kills'], r[4]['kills']]
        deaths = [r[0]['deaths'], r[1]['deaths'], r[2]['deaths'], r[3]['deaths'], r[4]['deaths']]
        assists = [r[0]['assists'], r[1]['assists'], r[2]['assists'], r[3]['assists'], r[4]['assists']]
        xpm = [r[0]['xp_per_min'], r[1]['xp_per_min'], r[2]['xp_per_min'], r[3]['xp_per_min'], r[4]['xp_per_min']]
        gpm = [r[0]['gold_per_min'], r[1]['gold_per_min'], r[2]['gold_per_min'], r[3]['gold_per_min'],
               r[4]['gold_per_min']]
        last_hits = [r[0]['last_hits'], r[1]['last_hits'], r[2]['last_hits'], r[3]['last_hits'], r[4]['last_hits']]
        duration = [r[0]['duration'], r[1]['duration'], r[2]['duration'], r[3]['duration'], r[4]['duration']]

        return f"""Averages Per Game: 
Kills: {round(mean(kills))}
Deaths: {round(mean(deaths))}
Assists: {round(mean(assists))}
XPM: {round(mean(xpm))}
GPM: {round(mean(gpm))}
LH: {round(mean(last_hits))}
Match Duration: {round(mean(duration) / 60)} mins"""
    else:
        return 'Invalid Response. Type $commands for help.'


def get_game_avg(player_id):
    name = player_id.lower()
    if name in players:
        r = requests.get(f' https://api.opendota.com/api/players/{players[name]}'
                         f'/recentMatches?api_key={api_key}')
        data = json.loads(r.text)
        values = 0
        for key in data:
            values += key['kills']
        avg = values / len(data)
        print(round(avg))


def get_kda_average(player_id):
    name = player_id.lower()
    if name in players:
        r = requests.get(f' https://api.opendota.com/api/players/{players[name]}'
                         f'/recentMatches?api_key={api_key}').json()
        data_length = len(r)
        kills = 0
        deaths = 0
        assists = 0
        for key in r:
            kills += key['kills']
            deaths += key['deaths']
            assists += key['assists']
        kills_avg = round(kills / data_length)
        deaths_avg = round(deaths / data_length)
        assists_avg = round(deaths / data_length)
        return f'Your average KDA is: {kills_avg}/{deaths_avg}/{assists_avg}'






