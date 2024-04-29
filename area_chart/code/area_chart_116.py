
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December'],
        'Social Media Users (in Millions)': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
        'Web Users (in Millions)': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot area chart
ax.stackplot(df['Month'], df['Social Media Users (in Millions)'], df['Web Users (in Millions)'], labels=['Social Media Users', 'Web Users'], alpha=0.8)

# Set x and y axis ticks and ticklabels with 70% probability
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(len(df)))
    ax.set_xticklabels(df['Month'])

if np.random.choice([True, False], p=[0.7, 0.3]):
    # Calculate max total value
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    # Ceil max_total_value up to the nearest multiple of 10, 100 or 1000
    if max_total_value < 100:
        max_total_value = np.ceil(max_total_value / 10) * 10
    elif max_total_value < 1000:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    # Set yticks with length in list of [3, 5, 7, 9, 11]
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    # Set yticklabels with rotation and wrap
    ax.set_yticklabels(['{:,.0f}'.format(x) for x in ax.get_yticks()], rotation=45, rotation_mode='anchor', ha='right')

# Set grid lines
ax.grid(alpha=0.3)

# Set title
ax.set_title('Social Media and Web Usage by Month')

# Set legend
ax.legend(loc='upper left')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-140159_27.png', bbox_inches='tight')

# Clear current image state
plt.clf()