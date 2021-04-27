from api_config import create_request
import pandas as pd



class MatchData:

    def __init__(self, match_id):
        self.id = match_id
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
