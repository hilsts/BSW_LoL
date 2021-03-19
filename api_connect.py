import requests
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['API']['key']

HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "{API_KEY}".format(API_KEY=API_KEY)
    }


class PlayerData:
    # TODO: get summoner data
    #       save summoner data

    def __init__(self, name):

        self.name = name
        self.account_id = self.get_account_id_by_name()
        self.summoner_id = self.get_summoner_id_by_name()
        self.get_matchlist_by_account_id()
        self.get_league_data_by_summoner()

    def get_summoner_id_by_name(self):
        """

        :return: account_id
        """

        get_account_id = requests.get('https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'.format(
            name=self.name), headers=HEADER)
        print('{name} summoner_id = '.format(name=self.name) + get_account_id.json()['id'])

        return get_account_id.json()['id']

    def get_account_id_by_name(self):
        """

        :return: account_id
        """

        get_account_id = requests.get('https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'.format(
            name=self.name), headers=HEADER)
        print('{name} account_id = '.format(name=self.name) + get_account_id.json()['accountId'])

        return get_account_id.json()['accountId']

    def get_matchlist_by_account_id(self):
        """

        :return: matchlist
        """

        get_match_list = requests.get(
            f'https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/{self.account_id}',
            headers=HEADER)
        print(get_match_list.json())
        print(len(get_match_list.json()['matches']))
        self.save_matchlist(get_match_list.json())

    def save_matchlist(self, matchlist_ob):
        """

        :param matchlist_ob: matchlist object from get_matchlist_by_account_id
        :return: file saving confirmation
        """

        df = pd.DataFrame(matchlist_ob['matches'])
        print(df.head(), df.size)
        df.to_csv(f'data/player_matchs/{self.name}.csv')
        print(f'file was saved in path: data/player_matchs/{self.name}.csv')

    def get_league_data_by_summoner(self):
        """

        :return:
        """

        summoner_data = requests.get(
            f'https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.summoner_id}',
            headers=HEADER)

        # print(f'/lol/league/v4/entries/by-summoner/{self.summoner_id}')
        print('summoner_data: '+ str(summoner_data.content))

class MatchData:

    def __init__(self, name):
        self.name = name
        self.match_list = self.read_matchlist()
        self.matches_data = self.get_matches_data()



    def read_matchlist(self):
        """

        :return:
        """

        match_list = pd.read_csv(f'data/player_matchs/{self.name}.csv')
        print(match_list['gameId'].unique().tolist())
        return match_list['gameId'].unique().tolist()


    def get_matches_data(self):
        """

        :return:
        """
        import json
        from datetime import date
        match_data_list = []
        for match in self.match_list:
            match_data = requests.get(f'https://br1.api.riotgames.com/lol/match/v4/matches/{match}', headers=HEADER)
            match_data_list.append(match_data.json())

        print(match_data_list)
        with open(f'data/matches/matches_raw/{self.name}_{str(date.today())}.txt', 'w') as outfile:
            json.dump(match_data_list, outfile)

PlayerData('Daft Mind')

