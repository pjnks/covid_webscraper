import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

response = requests.get('https://www.worldometers.info/coronavirus/country/us/')

soup = BeautifulSoup(response.text)

final = {'date': [], 'state': [], 'cases': []}
date = date.today()

states = soup.find_all('a', class_ = 'mt_a')
for state in states:
    final['state'].append(state.text)
    final['date'].append(date)
    final['cases'].append(date) #used date as a placeholder
    
df_final = pd.DataFrame(final)

df_final #preview dataframe
