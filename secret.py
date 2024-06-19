# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# # API_KEY = 'AIzaSyBfipCMGELAf4PepBy_7Csa-g3l5E44TJU'
import pandas as pd

# def fetch_secret(url, API_KEY):
#     gc = gspread.authorize(api_key=API_KEY)
#     sheet = gc.open_by_url(url).Sheet1

#     return sheet

# export fetch_secret
sheet_id = '1167qmFi18KOQSdksOnje0LLar3QO2WQoOGNNgFJ8_Ds'
sheet_name = 'Sheet1'
# sheet_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
sheet_url2 = f'https://docs.google.com/spreadsheets/d/{sheet_id}/edit?usp=sharing'

df = pd.read_csv(sheet_url2)
df

