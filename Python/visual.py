# Visualize Transfermarkt Arsenal Squad Data
from scrape import get_html, get_data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sort data by market value and position
def visualize(stats):
    print(stats) # debug

    # Numeric conversions
    total = pd.to_numeric(stats['Market Value']).sum()
    gk = pd.to_numeric(stats[stats['Group'] == 'Keeper']['Market Value']).sum()
    df = pd.to_numeric(stats[stats['Group'] == 'Defender']['Market Value']).sum()
    mf = pd.to_numeric(stats[stats['Group'] == 'Midfielder']['Market Value']).sum()
    fw = pd.to_numeric(stats[stats['Group'] == 'Forward']['Market Value']).sum()

    # Calculate the percentage of total market value by each position
    gk_per = gk / total
    df_per = df / total
    mf_per = mf / total
    fw_per = fw / total

    # Define custom colors
    colors = ['#EF3340', '#006400', '#FFD700', '#808080']

    # Create a figure and plot the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the pie chart
    labels = 'GK', 'DF', 'MF', 'FW'
    sizes = [gk_per, df_per, mf_per, fw_per]
    explode = (0.1, 0.1, 0.1, 0.1)
    ax.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%',
           colors=colors, shadow=True, startangle=90)
    ax.axis('equal')

    # Add a legend
    ax.legend(labels, loc='best')

    # Adjust the aspect ratio
    ax.set_aspect('equal')

    # Set the title with increased distance from the chart
    ax.set_title('Market Value by Position Group', pad=20, fontsize=16, fontweight='bold')

    # Save figure to folder location
    plt.savefig('C:/Users/jluki/workspace/Transfermarkt/Plot/visual.png')

    # Display the pie chart
    plt.show()

# main
if __name__ == '__main__':
    club = input('Which club would you like to analyze?: ')
    webpage = get_html(club)
    stats = get_data(webpage)
    visualize(stats)
