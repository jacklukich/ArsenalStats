# Python web scraping script to pull player data from transfermarkt.us
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from googlesearch import search

# Abbreviate position
def abbreviate_pos(pos):
    if pos == 'Goalkeeper':
        return 'GK'
    elif pos == 'Centre-Back':
        return 'CB'
    elif pos == 'Left-Back':
        return 'LB'
    elif pos == 'Right-Back':
        return 'RB'
    elif pos == 'Defensive Midfield':
        return 'DM'
    elif pos == 'Central Midfield':
        return 'CM'
    elif pos == 'Attacking Midfield':
        return 'AM'
    elif pos == 'Left Winger':
        return 'LW'
    elif pos == 'Right Winger':
        return 'RW'
    elif pos == 'Centre-Forward':
        return 'CF'
    else:
        return 'Unknown'
    
# Get position group
def get_pos_group(pos):
    if pos == 'GK':
        return 'Keeper'
    elif pos == 'CB' or pos == 'LB' or pos == 'RB':
        return 'Defender'
    elif pos == 'DM' or pos == 'CM' or pos == 'AM':
        return 'Midfielder'
    elif pos == 'LW' or pos == 'RW' or pos == 'CF':
        return 'Forward'
    else:
        return 'Unknown'
    
# Convert market value to proper float
def convert_mv(mv):
    if 'k' in mv:
        return float(mv[1:-1]) / 1000
    else:
        return float(mv[1:-1])

# Gets the HTML content of the webpage
def get_html(club):
    # Search Google for the club name followed by 'transfermarkt'
    query = f"{club} transfermarkt"
    search_results = list(search(query, num_results=1))

    if not search_results:
        print(f"Club '{club}' not found on Transfermarkt.")
        return None
    
    search_url = search_results[0]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table containing the player data
    return soup.find("table", class_="items")

# Get the player data
def get_data(table):
    # print('HTML TABLE: ', table)
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
        print('Data pulled successfully')
    else:
        print('Data pull failed')

    return pd.DataFrame(data)
