
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# data preprocessing
df = pd.DataFrame({
    'Category': ['Football', 'Basketball', 'Baseball', 'Soccer', 'Hockey', 'Tennis', 'Golf', 'Racing', 'Concerts', 'Theater'],
    'Number of Tickets Sold': [5000000, 3500000, 2000000, 3000000, 1500000, 1000000, 500000, 250000, 4000000, 3000000],
    'Revenue (Million USD)': [750, 550, 250, 500, 200, 150, 100, 50, 1000, 800],
    'Average Ticket Price (USD)': [150, 157, 125, 167, 133, 150, 200, 200, 250, 267]
})

# plot the heatmap chart
fig, ax = plt.subplots(figsize=(10, 7))
sns.heatmap(df.drop('Category', axis=1), cmap='Blues', annot=True, fmt='.2f', cbar=False, ax=ax)

# set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(3)+0.5)
ax.set_yticks(np.arange(10)+0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Category'], rotation=0, va='center')

# add a colorbar
cbar = ax.figure.colorbar(ax.collections[0])
cbar.ax.set_ylabel('Average Ticket Price (USD)', rotation=90, va='bottom')

# set the title
ax.set_title('Ticket Sales and Revenue by Sport/Event')

# adjust the layout and save the figure
fig.tight_layout()
fig.savefig('output/final/heatmap/png/20231228-131639_64.png', bbox_inches='tight')

# clear the current image state
plt.clf()