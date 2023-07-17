from scrape import get_html, get_data
from visual import visualize

# main
if __name__ == '__main__':
    club = input('Which club would you like to analyze?: ')
    webpage = get_html(club)
    stats = get_data(webpage)
    visualize(stats)
