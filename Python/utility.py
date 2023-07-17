# Miscellaneous internal functions
import pandas as pd

# Abbreviate position of a player
def abbreviate_pos(pos):
    if pos == 'Goalkeeper':
        return 'GK'
    elif pos == 'Centre-Back':
        return 'CB'
    elif pos == 'Left-Back':
        return 'LB'
    elif pos == 'Right-Back':
        return 'RB'
    elif pos == 'Defensive Midfield':
        return 'DM'
    elif pos == 'Central Midfield':
        return 'CM'
    elif pos == 'Attacking Midfield':
        return 'AM'
    elif pos == 'Left Winger':
        return 'LW'
    elif pos == 'Right Winger':
        return 'RW'
    elif pos == 'Centre-Forward':
        return 'CF'
    else:
        return 'Unknown'
    
# Get position group
def get_pos_group(pos):
    if pos == 'GK':
        return 'Keeper'
    elif pos == 'CB' or pos == 'LB' or pos == 'RB':
        return 'Defender'
    elif pos == 'DM' or pos == 'CM' or pos == 'AM':
        return 'Midfielder'
    elif pos == 'LW' or pos == 'RW' or pos == 'CF':
        return 'Forward'
    else:
        return 'Unknown'
    
# Convert market value to proper float
def convert_mv(mv):
    if 'k' in mv:
        return float(mv[1:-1]) / 1000 # converting thousands to millions
    elif 'm' in mv:
        return float(mv[1:-1]) # default (millions)
    else:
        return 0.0 # empty case
    
# Calculate the percentage of total market value by each position
def calculate_mv(stats):
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

# Calculate total market value
def mv_to_string(total):
    if total >= 1000:
        short_total = "{:.2f}".format(total/1000)
        return f'{short_total}bn' # billions
    elif total >= 1:
        short_total = "{:.2f}".format(total)
        return f'{short_total}m' # millions
    else:
        short_total = "{:.2f}".format(total*1000)
        return f'{short_total}k' # thousands
    
# Exporting data to CSV file
def export_data(stats, club):
    stats.to_csv(f'{club}_tm.csv', index=False)
