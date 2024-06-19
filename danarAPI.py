import requests as req
import json

API_KEY = '400687fa01104509801550973b3af716'
API_URL_TECH = f'https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey={API_KEY}'
API_URL_BUSINESS = f'https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey={API_KEY}'
API_URL_SPORTS = f'https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey={API_KEY}'
API_URL_HEALTH = f'https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey={API_KEY}'
API_URL_SCIENCE = f'https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey={API_KEY}'

# make it functional to reusable
def homePage() :
    print('----- Welcome! what kind of news that you want to see? -----')
    print('[1] Tech News')
    print('[2] Business News')
    print('[3] Sports News')
    print('[4] Sports News')
    print('[5] Science News')
    data = int(input('Input ur choice using number [1/2/3/4/5] : '))

    return data

# extract the data from the API using request.get (cause using GET Method)
def getData(API_URL):
    try:
        res = req.get(API_URL)
        
        # convert the object to dict in python, that seems like JSON in js
        data = res.json()

        # found the key == 'articles'
        if "articles" in data and isinstance(data["articles"], list):
            titles = data["articles"]

            # for gettin the title, where the key in nested object
            for i, title in enumerate(titles[:5]):
                title_article = title.get("title", "title not found")
                print(f"{i+1} - : {title_article}")
    except req.exceptions as e:
        print(str(e))

def execute():
    data = homePage()
    if data == 1:
        getData(API_URL_TECH)
    elif data == 2:
        getData(API_URL_BUSINESS)
    elif data == 3:
        getData(API_URL_SPORTS)
    elif data == 4:
        getData(API_URL_HEALTH)
    elif data == 5:
        getData(API_URL_SCIENCE)
    else:
        print(f"Number {data} is not in range!")

# Call that function to run the program
execute()


