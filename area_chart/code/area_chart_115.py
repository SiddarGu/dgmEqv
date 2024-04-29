
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'Category': ['Ancient', 'Medieval', 'Renaissance', 'Modern'],
        'History (%)': [20, 15, 25, 30],
        'Psychology (%)': [25, 30, 20, 25],
        'Political Science (%)': [15, 20, 25, 25],
        'Anthropology (%)': [20, 25, 15, 10],
        'Literature (%)': [20, 10, 15, 10]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 6))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Round up max total value to nearest multiple of 10, 100 or 1000
if max_total_value < 10:
    max_total_value = np.ceil(max_total_value)
elif max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y limit and ticks
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
plt.ylim(0, max_total_value)
plt.yticks(yticks)

# Plot data as stacked area chart
ax = plt.stackplot(df['Category'], df['History (%)'], df['Psychology (%)'], df['Political Science (%)'], df['Anthropology (%)'], df['Literature (%)'], labels=['History', 'Psychology', 'Political Science', 'Anthropology', 'Literature'], colors=['#ff8c00', '#8b4513', '#008000', '#2f4f4f', '#000080'], alpha=0.7)

# Set x limit and ticks
plt.xlim(0, len(df.index) - 1)
plt.xticks(range(len(df.index)), df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Add grid lines
plt.grid(color='#d3d3d3', linestyle='--', linewidth=0.5)

# Add legend
plt.legend(loc='upper left')

# Add title
plt.title('Influence of Social Sciences and Humanities through Time')

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-140159_24.png', bbox_inches='tight')

# Clear current image state
plt.clf()