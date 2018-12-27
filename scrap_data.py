import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

data = requests.get('https://perlas.lt/lt/statistic/vikinglotto?tab=archive&Filter%5BdrawFrom%5D=1343&Filter%5BdrawTo%5D=1343')

soup = BeautifulSoup(data.text, 'html.parser')

table = soup.find('table', { 'class': 'table' })
tirazas = soup.find('p', {'class': 'lead'}).text.strip()
tirazas = tirazas[13:]
date = table.find('td').text.strip()
numbers = table.find_all('li', {'class': 'number'})[0].text.strip()
numbers1 = table.find_all('li', {'class': 'number'})[1].text.strip()
numbers2 = table.find_all('li', {'class': 'number'})[2].text.strip()
numbers3 = table.find_all('li', {'class': 'number'})[3].text.strip()
numbers4 = table.find_all('li', {'class': 'number'})[4].text.strip()
numbers5 = table.find_all('li', {'class': 'number'})[5].text.strip()
papildomi_skaiciai1 = table.find_all('li', {'class': 'number bonus-number'})[0].text.strip()
#papildomi_skaiciai2 = table.find_all('li', {'class': 'number bonus-number'})[1].text.strip()
#auksinis_skaicius = table.find_all('td')[5].text.strip()

result = pd.DataFrame([[date, tirazas, [int(numbers), int(numbers1),int(numbers2),int(numbers3),int(numbers4),int(numbers5)],papildomi_skaiciai1]])
result.columns = ['date', 'tirazas', 'skaiciai', 'vikingo_skaicius']
result.to_csv('skaiciai.csv')
print(result)
