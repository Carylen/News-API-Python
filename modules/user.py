from dataclasses import dataclass, asdict
# import json

# from dataclasses import dataclass
# API_KEY = 'AIzaSyBfipCMGELAf4PepBy_7Csa-g3l5E44TJU'
# api_key = os.environ.get('AIzaSyBfipCMGELAf4PepBy_7Csa-g3l5E44TJU')
# sheet_id = '1167qmFi18KOQSdksOnje0LLar3QO2WQoOGNNgFJ8_Ds'
# spread_id = '1167qmFi18KOQSdksOnje0LLar3QO2WQoOGNNgFJ8_Ds'
# sheet_id = '0'
# sheet_name = 'Sheet1'
# url = f'https://sheets.googleapis.com/v4/spreadsheets/{spread_id}/values/{sheet_name}?key={api_key}'

# response = requests.get(url)
# df = pd.read_csv(url)
# print(url)
# print(df)

@dataclass
class User:
    name: str
    age: int
    phoneNumber: str

    def to_dict(self):
        return asdict(self)
