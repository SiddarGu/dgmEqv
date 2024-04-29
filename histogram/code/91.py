import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Region': ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania'],
    'Internet Users (Millions)': [725.5, 847.2, 1598.3, 345.7, 216.0, 110.2]
}

# Creating DataFrame from data
df = pd.DataFrame(data)

# Set fig size
plt.figure(figsize=(10, 8))

# Adding subplot
ax = plt.subplot()

# Plotting vertical histogram
df.plot(kind='bar', x='Region', y='Internet Users (Millions)', legend=False, ax=ax)

# Title
plt.title('Regional Distribution of Internet Users Worldwide')

# Set background grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Label management to prevent overlap
ax.set_xticklabels(df['Region'], rotation=45, horizontalalignment='right')

# Tight layout to fit the figure neatly
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/91.png')

# Clear the current figure state
plt.clf()
