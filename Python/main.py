# Main flow of the program
from input import get_club, get_export, get_vis_mv, get_vis_players
from scrape import find_club, get_table, get_data

# main
if __name__ == '__main__':
    club = get_club()
    club_url, club = find_club(club)
    webpage = get_table(club_url)
    stats = get_data(webpage)
    # Visualization and exportation input sequence (refactor out later)
    get_export(stats, club)
    get_vis_mv(stats)
    get_vis_players(stats)
