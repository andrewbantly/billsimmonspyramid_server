from requests import get
import json
from bs4 import BeautifulSoup

url = "https://www.basketball-reference.com/awards/simmons_pyramid.html"

r = get(url)

soup = BeautifulSoup(r.content, "html.parser")

# Creating list with all tables
tables = soup.find_all('table')

#  Looking for the table with the classes 'wikitable' and 'sortable'
table = soup.find('table', class_='stats_table')

# initialize the data
data = []

# collecting data
for row in table.tbody.find_all('tr'):
    # find all data for each column
    columns = row.find_all('td')
    rank = row.find_all('th')
    if rank != []:
        ranking = rank[0].text.strip()
    if columns != []:
        player = columns[0].text.strip()
        debut = columns[1].text.strip()
        final = columns[2].text.strip()
        games = columns[3].text.strip()
        minutes = columns[4].text.strip()
        points = columns[5].text.strip()  
        rebounds = columns[6].text.strip()
        assists = columns[7].text.strip()    
        steals = columns[8].text.strip()
        blocks = columns[9].text.strip()
        fg_percentage = columns[10].text.strip()
        three_percentage = columns[11].text.strip()  
        ft_percentage = columns[12].text.strip()
        winshare = columns[13].text.strip()
        winshareper48 = columns[14].text.strip()

        data.append({
            'Rank': ranking,
            'Player': player,
            'From': debut,
            'To': final,
            'Games': games,
            'Minutes Played Per Game': minutes,
            'Points Per Game': points,
            'Total Rebounds Per Game': rebounds,
            'Assists Per Game': assists,
            'Steals Per Game': steals,
            'Blocks Per Game': blocks,
            'Field Goal Percentage': fg_percentage,
            '3-Point Field Goal Percentage': three_percentage,
            'Free Throw Percentage': ft_percentage,
            'Win Shares': winshare,
            'Win Shares Per 48 Minutes': winshareper48
        })

with open('original_pyramid.json', 'w', encoding='UTF8') as f:
    json.dump(data, f)


print("done")