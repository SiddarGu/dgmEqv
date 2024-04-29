
# Solution

# Import necessary modules
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data as dictionary
data = {'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
        'Facebook (Users)': [100, 120, 140, 160, 180, 200],
        'Twitter (Users)': [80, 100, 120, 130, 140, 150],
        'Instagram (Users)': [120, 150, 170, 190, 210, 230],
        'LinkedIn (Users)': [60, 70, 80, 90, 100, 110],
        'YouTube (Users)': [150, 170, 190, 210, 230, 250]}

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set colors and transparency
colors = ['lightcoral', 'skyblue', 'lightgreen', 'plum', 'gold']
alpha = 0.6

# Plot area chart with stackplot
ax.stackplot(df['Month'], df['Facebook (Users)'], df['Twitter (Users)'], df['Instagram (Users)'], df['LinkedIn (Users)'], df['YouTube (Users)'],
             labels=['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'YouTube'], colors=colors, alpha=alpha)

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, df.iloc[:, 1:].sum(axis=1).max())
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_xticklabels(df['Month'], rotation=45, ha='right', rotation_mode='anchor')
ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))

# Set grid lines
ax.grid(linewidth=0.5, color='lightgray')

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title and labels
ax.set_title('User Distribution on Social Media Platforms by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Users')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_85.png', bbox_inches='tight')

# Clear image state
plt.clf()