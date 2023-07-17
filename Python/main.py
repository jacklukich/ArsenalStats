# Main flow of the program
from input import i_club, i_export
from scrape import find_club, get_table, get_data
from visual import visualize_mv

# main
if __name__ == '__main__':
    club = i_club()
    club_url = find_club(club)
    webpage = get_table(club_url)
    stats = get_data(webpage)
    i_export(stats, club)
    visualize_mv(stats)

