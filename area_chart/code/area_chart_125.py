
# Import required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary from data
data = {'Category': ['Sports', 'Basketball', 'Soccer', 'Baseball', 'Hockey', 'Tennis', 'Golf', 'Music', 'Comedy', 'Drama', 'Action', 'Documentary', 'Food'], 
        'Events': [100, 150, 100, 200, 150, 180, 130, 250, 120, 180, 150, 120, 100], 
        'Concerts': [120, 180, 200, 180, 200, 150, 100, 130, 100, 200, 180, 150, 200], 
        'Theater': [150, 200, 250, 150, 100, 100, 150, 100, 200, 150, 130, 200, 250], 
        'Movies': [100, 150, 180, 130, 250, 200, 180, 200, 180, 100, 200, 170, 150], 
        'Festivals': [200, 250, 150, 100, 120, 170, 200, 150, 150, 250, 100, 130, 180]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data
fig, ax = plt.subplots(figsize=(12, 8))

# Set random background grid lines
ax.grid(color='grey', linestyle='--', linewidth=0.5)

# Set title
plt.title('Event Distribution by Category')

# Plot the area chart
ax.stackplot(df['Category'], df['Events'], df['Concerts'], df['Theater'], df['Movies'], df['Festivals'], labels=['Events', 'Concerts', 'Theater', 'Movies', 'Festivals'])

# Set legend
ax.legend(loc='upper left')

# Set x and y axis ticks and ticklabels
if np.random.randint(1, 11) <= 7:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Category'])

if np.random.randint(1, 11) <= 7:
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-140159_36.png', bbox_inches='tight')

# Clear the current image state
plt.clf()