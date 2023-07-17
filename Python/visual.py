# Visualize Transfermarkt Arsenal Squad Data
import matplotlib.pyplot as plt
import pandas as pd
from utility import mv_to_string

# Calculate the percentage of total market value by each position
def calculate(stats):
    # Numeric conversions
    total = pd.to_numeric(stats['Market Value']).sum()
    gk = pd.to_numeric(stats[stats['Group'] == 'Keeper']['Market Value']).sum()
    df = pd.to_numeric(stats[stats['Group'] == 'Defender']['Market Value']).sum()
    mf = pd.to_numeric(stats[stats['Group'] == 'Midfielder']['Market Value']).sum()
    fw = pd.to_numeric(stats[stats['Group'] == 'Forward']['Market Value']).sum()

    # Add values to list
    nums = []
    nums.append(gk / total)
    nums.append(df / total)
    nums.append(mf / total)
    nums.append(fw / total)

    return nums, total

# Visualize the data
def visualize(nums, total):
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
