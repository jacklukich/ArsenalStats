# Input handling
from utility import export_data

# Get club input from user
def i_club():
    return input('Which club would you like to analyze?: ')

# Ask user if they would like to export the club's data to a CSV file
def i_export(stats, club):
    response = input('Would you like to export this data to a CSV file? (y/n): ')
    while response != 'y' and response != 'n':
        print('Error - please enter y or n.')
        response = input('Would you like to export this data to a CSV file? (y/n): ')

    if response == 'y':
        print('Exporting data..')
        export_data(stats, club)
    else:
        print('Not exporting data..')
