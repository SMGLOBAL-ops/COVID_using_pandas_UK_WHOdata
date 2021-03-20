import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import urllib.request


url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
file_path = os.path.join("data", "covid")

os.makedirs(file_path, exist_ok=True)
csv_path = os.path.join(file_path, "WHO-COVID-19-global-data.csv")
urllib.request.urlretrieve(url, csv_path)
df = pd.read_csv(csv_path)

#1

Date_reported1 = df.loc[(df.New_deaths > 1000) & (df.Country_code == 'GB')][ "Date_reported"]

Cumulative_deaths = df.loc[(df.New_deaths > 1000) & (df.Country_code == 'GB')][ "Cumulative_deaths"]

#print(Date_reported1, Cumulative_deaths)

#plt.plot(Date_reported1, Cumulative_deaths)

#2

Date_reported2 = df.loc[(df.Country_code == 'GB')]['Date_reported']

New_deaths = df.loc[(df.Country_code == 'GB')]['New_deaths']

print(Date_reported2)
print(New_deaths)

plt.title('COVID-19 New Deaths reported per day in The United Kingdom')
plt.xlabel('Days since start of pandemic in The United Kingdom')
plt.ylabel('Number of reported Deaths')


plt.plot(Date_reported2, New_deaths, label='Latest data from The WHO')
plt.legend()
plt.show()
