import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.8635&lon=-81.6765#.XptflsgzbIU')
soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(id='seven-day-forecast')
# print(week)
items = week.find_all(class_='tombstone-container')

# print(items[0].find(class_="period-name").get_text())

# print(items[0].find(class_="short-desc").get_text())
# print(items[0].find(class_="temp").get_text())

period_name = [item.find(class_='period-name').get_text() for item in items]
sort_dec =  [item.find(class_='short-desc').get_text() for item in items]
tempareture =  [item.find(class_='temp').get_text() for item in items]

# print(period_name)
# print(sort_dec)
# print(tempareture)



weather_staff = pd.DataFrame(
    {
        'period_name' : period_name,
        'sort_dec' : sort_dec,
        'tempareture' :tempareture


    }
)


print(weather_staff)
weather_staff.to_csv('weather.csv')