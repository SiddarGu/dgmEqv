
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import seaborn for heatmap plot
import seaborn as sns

# Set font size
plt.rcParams['font.size'] = 11

# Set figure size
fig, ax = plt.subplots(figsize=(8, 6))

# Create data dictionary
data = {'Team': ['Lakers', 'Yankees', 'Cowboys', 'Real Madrid', 'Red Sox', 'Patriots'],
        'Sport': ['Basketball', 'Baseball', 'Football', 'Soccer', 'Baseball', 'Football'],
        'Revenue ($ Million)': [375, 300, 450, 500, 300, 450],
        'Ticket Sales ($ Million)': [150, 100, 200, 150, 100, 200],
        'Merchandise Sales ($ Million)': [100, 50, 150, 100, 50, 150],
        'TV Rights ($ Million)': [75, 100, 50, 150, 100, 50],
        'Sponsorship ($ Million)': [50, 50, 100, 100, 50, 100]}

# Convert data dictionary to dataframe
df = pd.DataFrame(data)

# Set index and columns for dataframe
df = df.set_index(['Team', 'Sport'])

# Create heatmap using seaborn
sns.heatmap(df, annot=True, fmt='.0f', cmap='Blues', cbar=False)

# Set x and y ticks and labels
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_yticks(np.arange(0.5, len(df.index), 1))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor', wrap=True)

# Set ticks and ticklabels in the center of rows and columns
ax.tick_params(axis='both', which='both', length=0)
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns, ha='center')
ax.set_yticklabels(df.index, va='center')

# Set title of the figure
ax.set_title('Revenue Breakdown by Sport and Team')

# Automatically resize image by tight_layout()
plt.tight_layout()

# Save figure as png
plt.savefig('output/final/heatmap/png/20231228-162116_18.png', bbox_inches='tight')

# Clear current image state
plt.clf()