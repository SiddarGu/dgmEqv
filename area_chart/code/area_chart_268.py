
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Convert data to a dictionary
data = {
    'Year': [2016, 2017, 2018, 2019, 2020],
    'Criminology (Degrees)': [500, 550, 600, 650, 700],
    'Psychology (Degrees)': [600, 650, 700, 750, 800],
    'Sociology (Degrees)': [400, 450, 500, 550, 600],
    'Anthropology (Degrees)': [300, 350, 400, 450, 500],
    'Linguistics (Degrees)': [200, 250, 300, 350, 400]
}

# Convert data to a dataframe
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12,8))

# Set axes
ax = fig.add_subplot(111)

# Set x and y ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')
ax.tick_params(axis='y', labelsize=14)

# Calculate max total value and set y limits and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set colors and transparency
colors = ['#f7c8c8', '#a1d1e7', '#f8d9b8', '#b7e1cd', '#f5e5a3']
alpha = 0.8

# Plot the data as an area chart
ax.stackplot(df.index, df.iloc[:, 1:].T, labels=df.columns[1:], colors=colors, alpha=alpha)

# Set background grid lines
ax.grid(axis='y', color='#d4d4d4')

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Number of Degrees Awarded in Social Sciences and Humanities from 2016 to 2020', fontsize=18)

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-155112_29.png', bbox_inches='tight')

# Clear current image state
plt.clf()