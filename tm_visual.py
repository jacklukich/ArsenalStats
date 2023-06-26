# Visualize Transfermarkt Arsenal Squad Data
from tm_script import parse_webpage, get_data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Sort data by market value and position
def visualize(stats):
    # Sort the data
    stats = stats.sort_values(by=['Market Value'], ascending=False)
    stats = stats.sort_values(by=['Group'])

    # Convert total and gk to numeric types
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

    # Create a figure and plot the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the pie chart
    labels = 'GK', 'DF', 'MF', 'FW'
    sizes = [gk_per, df_per, mf_per, fw_per]
    explode = (0.1, 0.1, 0.1, 0.1)
    ax.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%',
           shadow=False, startangle=90)
    ax.axis('equal')

    # Set the title with increased distance from the chart
    ax.set_title('Market Value by Position Group', pad=20)

    # Remove the axes and ticks for a cleaner look
    ax.axis('off')

    # Display the pie chart
    plt.show()

# main
if __name__ == '__main__':
    webpage = parse_webpage()
    stats = get_data(webpage)
    visualize(stats)
