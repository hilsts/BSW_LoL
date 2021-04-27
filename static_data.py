from api_config import create_request
import pandas as pd

def get_champions():

    r = create_request('http://ddragon.leagueoflegends.com/cdn/11.6.1/data/en_US/champion.json')
    data = r.json()['data']
    temp_list = []
    for key in data.keys():
        temp_list.append(data[key])
    df = pd.DataFrame(temp_list)
    df.to_csv('data/static/champions.csv')
    print('file saved in data/static/champions.csv')


get_champions()