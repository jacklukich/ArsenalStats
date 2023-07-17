from input import get_club
from scrape import find_club, get_table, get_data
from visual import calculate, visualize

# main
if __name__ == '__main__':
    club = get_club()
    club_url = find_club(club)
    webpage = get_table(club_url)
    stats = get_data(webpage)
    values, total = calculate(stats)
    visualize(values, total)
