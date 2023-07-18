# Visualization of Data
import matplotlib.pyplot as plt
import pandas as pd
from utility import calculate_mv, mv_to_string

# Visualize market value data
def visualize_mv(stats):
    # Get necessary stats
    nums, total = calculate_mv(stats)

    # Define custom colors
    colors = ['#EF3340', '#006400', '#FFD700', '#808080']

    # Create a figure and plot the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the pie chart
    labels = 'GK', 'DF', 'MF', 'FW'
    sizes = [nums[0], nums[1], nums[2], nums[3]]
    explode = (0.1, 0.1, 0.1, 0.1)
    ax.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%',
           colors=colors, shadow=True, startangle=90, radius=0.7)
    ax.axis('equal')

    # Add a legend
    ax.legend(labels, loc='best')

    # Adjust the aspect ratio
    ax.set_aspect('equal')

    # Adding sub-text to display club's total market value
    sub_text = f"Total Club Market Value: €{mv_to_string(total)}" 
    ax.text(0.5, -0.1, sub_text, fontsize=12, ha='center', transform=ax.transAxes)

    # Set the title with increased distance from the chart
    ax.set_title('Market Value by Position Group', pad=20, fontsize=16, fontweight='bold')

    # Display the pie chart
    plt.show()

    # Print complete message
    print('Visualization complete.')


# Visualize plyer data
def visualize_players(players, stats):
    # find rows for each player
    
    # create a figure and plot the bar chart

       # add a legend

       # set the title with increased distance from the chart

       # display the bar chart

    return None