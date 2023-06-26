# Python web scraping script to pull player data from transfermarkt.us
import os
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

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

# Parse the webpage
def parse_webpage():
    url = 'https://www.transfermarkt.us/arsenal-fc/kader/verein/11/saison_id/2022/plus/1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the player data
    return soup.find('table', class_='items')

# Get the player data
def get_data(table):
    # Extract the player data
    data = []
    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')

        # Check if all required columns exist
        if len(columns) < 13:
            continue

        # grab actual data
        name = columns[3].text.strip()
        position = abbreviate_pos(columns[4].text.strip())
        group = get_pos_group(position)
        age = columns[5].text.strip().split()[-1][1:-1]
        market_value = columns[12].text.strip()[1:-1]

        data.append({
            'Name': name,
            'Position': position,
            'Group': group,
            'Age': age,
            'Market Value': market_value
        })
    
    # DEBUG: print the data
    # print(data)

    # Return dataframe
    # print('Data pulled successfully')
    return pd.DataFrame(data)