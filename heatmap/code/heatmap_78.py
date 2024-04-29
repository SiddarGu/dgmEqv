
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
data = {'Team': ['Los Angeles Lakers', 'New York Yankees', 'Chicago Bulls', 'Dallas Cowboys', 'Manchester United'],
        'Player Salaries (Millions)': [100, 80, 70, 90, 60],
        'Ticket Sales (Millions)': [500, 450, 400, 600, 300],
        'Merchandise Sales (Millions)': [200, 150, 120, 180, 100],
        'Advertising Revenue (Millions)': [300, 250, 220, 350, 200],
        'TV Deals (Millions)': [800, 750, 700, 900, 600]}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Set team name as index
df.set_index('Team', inplace=True)

# Create heatmap chart using seaborn
import seaborn as sns
fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(df, annot=True, fmt='g', cmap='Blues', linewidths=0.5, cbar=False)

# Set ticks and ticklabels for x and y axis, and make them in the center of rows and columns
ticklabels = [x[:6] if len(x) > 6 else x for x in df.columns]
ax.set_xticklabels(ticklabels, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ticklabels[::-1], rotation=0, ha='right', rotation_mode='anchor')

# Add title to the chart
plt.title('Sports Team Revenue Breakdown')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save figure as png
plt.savefig('output/final/heatmap/png/20231228-124154_7.png', bbox_inches='tight')

# Clear the current image state
plt.clf()
plt.close()