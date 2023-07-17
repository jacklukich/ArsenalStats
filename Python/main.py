from scrape import find_club, get_table, get_data
from visual import calculate, visualize

# main
if __name__ == '__main__':
    club = input('Which club would you like to analyze?: ')
    club_url = find_club(club)
    webpage = get_table(club_url)
    stats = get_data(webpage)
    values, total = calculate(stats)
    visualize(values, total)
