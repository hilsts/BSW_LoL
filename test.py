from api_config import create_request
import pandas as pd
import time
import json

LEAGUES = ['DIAMOND', 'PLATINUM', 'GOLD', 'SILVER', 'BRONZE', 'IRON']
DIVISIONS = ['I', 'II', 'III', 'IV']

# TODO: Tornar código não tóxico

def get_league_by_division(league):

    temp_list = []
    for div in DIVISIONS:
        url = f'https://br1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{league}/{div}'
        r = create_request(url)

        df = pd.DataFrame(r.json())
        print(df.shape)
        print(f'Ligas únicas na divisão {div}: ' + str(len(df['leagueId'].unique())))
        print('Total de jogadores: ' + str(len(df['summonerId'].unique().tolist())))

        print('\n')
        temp_list += df['leagueId'].unique().tolist()


    print('temp_list size: ' + str(len(temp_list)))
    print('temp_list_set size: ' + str(len(list(set(temp_list)))))
    return list(set(temp_list))

def get_players_by_league(league_ids, league):

    league_data_list = []
    request_num = 0
    for league_id in league_ids:
        r = create_request(f'https://br1.api.riotgames.com/lol/league/v4/leagues/{league_id}')
        if r.status_code == 200:
            print(f'liga {league_id}')
            league_data_list.append(r.json())
        else:
            request_num+=1
            print(f'salvando {str(len(league_data_list))} registros em data/raw/{league}_{request_num}.txt')
            f = open(f'data/raw/{league}_{request_num}.txt', 'w')
            f.write(json.dumps(league_data_list))
            f.close()
            print('dormindo.....')
            time.sleep(120)
            print('acordando.....')
            league_data_list = []
            continue

    request_num += 1
    print(f'salvando {str(len(league_data_list))} registros em data/raw/{league}_{request_num}.txt')
    f = open(f'data/raw/{league}_{request_num}.txt', 'w')
    f.write(json.dumps(league_data_list))
    f.close()
    print('dados salvos')

league = 'PLATINUM'
diamond_leagues = get_league_by_division(league)
get_players_by_league(diamond_leagues, league)