
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Process the data using dict and pandas
data = {'Sport': ['Football', 'Basketball', 'Baseball', 'Soccer', 'Tennis'],
        'Athleticism (%)': [70, 75, 80, 85, 90],
        'Strategy (%)': [60, 65, 70, 75, 80],
        'Teamwork (%)': [80, 85, 90, 95, 98],
        'Endurance (%)': [75, 80, 85, 90, 93],
        'Creativity (%)': [50, 55, 60, 65, 70],
        'Outlook (%)': [90, 93, 95, 98, 99]}

df = pd.DataFrame(data)

# Set the figure size
fig = plt.figure(figsize=(10, 8))

# Plot the heatmap chart using seaborn
ax = sns.heatmap(df.iloc[:, 1:], annot=True, cmap='Blues', linewidths=0.5)

# Set the title
plt.title('Team Performance in Different Sports')

# Set the ticks and tick labels for x and y axis
ax.set_xticks(np.arange(len(df.columns) - 1) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df['Sport'])) + 0.5)
ax.set_yticklabels(df['Sport'], rotation=0, ha='right', rotation_mode='anchor')

# Center the ticks and tick labels for x and y axis
ax.tick_params(left=False, bottom=False)
ax.set_xticks(np.arange(len(df.columns) - 1) + 0.5, minor=True)
ax.set_yticks(np.arange(len(df['Sport'])) + 0.5, minor=True)
ax.tick_params(which='minor', left=True, bottom=True)
ax.grid(False, which='minor')

# Automatically resize the image
fig.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-124154_78.png', bbox_inches='tight')

# Clear the current figure state
plt.clf()