# Web-scraping logic
import requests
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
from googlesearch import search
from utility import abbreviate_pos, get_pos_group, convert_mv

# Getting the club name from Transfermarkt URL
def _extract_club(url):
    parts = url.split('/')
    return parts[-4].replace('-', ' ').title() # replace hyphens with spaces

# Search google to find correct club page on transfermarkt
def find_club(club):
    query = f"{club} transfermarkt"
    search_results = list(search(query, num_results=1))

    if not search_results:
        print(f"Club '{club}' not found on Transfermarkt.")
        return None
    else:
        print(f"Identified club: {_extract_club(search_results[0])}")
    
    return search_results[0], _extract_club(search_results[0])

# Gets the main table containing player information from webpage
def get_table(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table containing the player data
    return soup.find("table", class_="items")

# Extract player data from main HTML table
def get_data(table):
    data = []
    for player in table.find_all('tr')[1:]:
        player_info = player.find_all('td')[1:]

        # Check if all required columns exist (8 total)
        if len(player_info) < 8:
            continue

        # grab actual data
        name = player_info[2].find('a').text.strip()
        position = abbreviate_pos(player_info[3].text.strip())
        group = get_pos_group(position)
        age = player_info[5].text.strip().split('(')[-1].strip(')')
        market_value = convert_mv(player_info[7].text.strip())

        data.append({
            'Name': name,
            'Position': position,
            'Group': group,
            'Age': age,
            'Market Value': market_value
        })
   
    if data:
        print('Data pulled successfully.')
    else:
        print('Data pull failed.')

    return pd.DataFrame(data)
