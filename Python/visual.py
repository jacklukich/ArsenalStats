# Visualize Transfermarkt Arsenal Squad Data
import matplotlib.pyplot as plt
import pandas as pd

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

    return nums

# Visualize the data
def visualize(nums):
    # Define custom colors
    colors = ['#EF3340', '#006400', '#FFD700', '#808080']

    # Create a figure and plot the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the pie chart
    labels = 'GK', 'DF', 'MF', 'FW'
    sizes = [nums[0], nums[1], nums[2], nums[3]]
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

    # Display the pie chart
    plt.show()

    # Print complete message
    print('Visualization complete.')
