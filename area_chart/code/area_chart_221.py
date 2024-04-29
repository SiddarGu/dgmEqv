
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set data
data = {
    'Category': ['Internet Users (in millions)', 'Mobile Users (in millions)'],
    'Q1': [250, 100],
    'Q2': [280, 120],
    'Q3': [300, 150],
    'Q4': [320, 180]
}


# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figsize
plt.figure(figsize=(10, 6))

# Set colors and transparency
colors = ['#FF6347', '#6A5ACD', '#7FFF00', '#32CD32']
alpha = 0.8

# Set max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10

# Set yticks
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)

# Plot area chart
ax = plt.gca()
ax.stackplot(df['Category'], df.iloc[:, 1:].values.transpose(), labels=df.columns[1:], colors=colors, alpha=alpha)

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, rotation=45, ha='right', rotation_mode='anchor')

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set legend position
ax.legend(loc='upper left')

# Set title
plt.title('Internet and Mobile Users in 2020')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-145339_64.png', bbox_inches='tight')

# Clear current image state
plt.clf()