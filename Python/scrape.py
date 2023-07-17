# Python web scraping script to pull player data from transfermarkt.us
import requests
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
from googlesearch import search

# Abbreviate position
def _abbreviate_pos(pos):
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
def _get_pos_group(pos):
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
def _convert_mv(mv):
    if 'k' in mv:
        return float(mv[1:-1]) / 1000
    elif 'm' in mv:
        return float(mv[1:-1])
    else:
        return None

# Search google to find correct club page on transfermarkt
def find_club(club):
    query = f"{club} transfermarkt"
    search_results = list(search(query, num_results=1))

    if not search_results:
        print(f"Club '{club}' not found on Transfermarkt.")
        return None
    
    return search_results[0]

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
        position = _abbreviate_pos(player_info[3].text.strip())
        group = _get_pos_group(position)
        age = player_info[5].text.strip().split('(')[-1].strip(')')
        market_value = _convert_mv(player_info[7].text.strip())

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
