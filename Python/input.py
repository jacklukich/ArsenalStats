# Input handling
from utility import export_data, valid_response
from visual import visualize_mv, visualize_players

# Get club input from user
def get_club():
    return input('Which club would you like to analyze?: ')

# Ask user if they would like a CSV file
def get_export(stats, club):
    response = input('Would you like to export this data to a CSV file? (y/n): ')
    while response != 'y' and response != 'n':
        print('Error - please enter y or n.')
        response = input('Would you like to export this data to a CSV file? (y/n): ')

    if response == 'y':
        print('Exporting data..')
        export_data(stats, club)

# Ask user if they want market value data visualized
def get_vis_mv(stats):
    response = input('Would you like to visualize the club\'s market value data? (y/n): ')
    while response != 'y' and response != 'n':
        print('Error - please enter y or n.')
        response = input('Would you like to visualize the club\'s market value data? (y/n): ')
    if response == 'y':
        print('Visualizing club market value data..')
        visualize_mv(stats)

# Sequence of getting players
def _find_players(stats):
    response = input('Enter the full names of the players you would like to compare (separated by commas): ')
    stats.set_index('Name', inplace=True)
    while not valid_response(response, stats):
        print('Invalid player name(s). Please try again: ')
        response = input('Enter the full names of the players you would like to compare (separated by commas): ')
    players = response.split(',')
    return players

# Ask user if they want to compare two players visually
def get_vis_players(stats):
    response = input('Would you like to compare two players visually? (y/n): ')
    while response != 'y' and response != 'n':
        print('Error - please enter y or n.')
        response = input('Would you like to compare two players visually? (y/n): ')
    if response == 'y':
        players = _find_players(stats)
        print('DEBUG: players = ', players)
        print(f'Visualizing {players[0]} vs. {players[1]}..')
        visualize_players(players, stats)
