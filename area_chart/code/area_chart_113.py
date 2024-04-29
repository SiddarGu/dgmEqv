
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Convert data to dictionary
data = {'Category': ['Psychology', 'Sociology', 'History', 'Anthropology', 'Political Science'],
        '2000': [1000, 800, 900, 700, 600],
        '2001': [1100, 900, 1000, 800, 700],
        '2002': [1200, 1000, 1100, 900, 800],
        '2003': [1300, 1100, 1200, 1000, 900],
        '2004': [1400, 1200, 1300, 1100, 1000],
        '2005': [1500, 1300, 1400, 1200, 1100],
        '2006': [1600, 1400, 1500, 1300, 1200],
        '2007': [1700, 1500, 1600, 1400, 1300],
        '2008': [1800, 1600, 1700, 1500, 1400],
        '2009': [1900, 1700, 1800, 1600, 1500],
        '2010': [2000, 1800, 1900, 1700, 1600]}

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Round up max total value to nearest multiple of 10, 100, or 1000
if max_total_value <= 10:
    max_total_value = 10
elif max_total_value <= 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value <= 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y-axis limits and ticks
# yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
# plt.yticks(yticks)
# plt.ylim(0, max_total_value)

# Set colors and transparency
colors = ['#B2DFDB', '#F0F4C3', '#FFCCBC', '#FFAB91', '#BCAAA4']
alpha = 0.7

# Set background grid lines
plt.grid(color='#BDBDBD', linestyle=':', axis='y', alpha=0.5)

# Plot area chart
ax = plt.gca()
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=df.columns[1:], colors=colors, alpha=alpha)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set x-axis ticks and tick labels
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.xlim(0, len(df.index) - 1)

# Set title and labels
plt.title('Publication Trends in Social Sciences and Humanities per Year')
plt.xlabel('Year')
plt.ylabel('Publications')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-140159_21.png', bbox_inches='tight')

# Clear current image state
plt.clf()