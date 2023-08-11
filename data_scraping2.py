from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

table_rows = star_table[7].find_all('tr')
t_list = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    t_list.append(row)

Star_name = []
Distance = []
Radius = []
Mass = []

for i in range(1,len(t_list)):
    Star_name.append(t_list[i][1])
    Distance.append(t_list[i][3])
    Mass.append(t_list[i][5])
    Radius.append(t_list[i][6])

df2 = pd.DataFrame(list(zip(Star_name,Distance,Mass,Radius)), columns=('Star_name','Distance','Mass','Radius'))
print(df2)

df2.to_csv('bright_stars.csv')