
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Convert data to a dictionary
data = {'Category': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania'],
        'Corn Production (units)': [1000, 800, 1200, 900, 600, 500],
        'Soybean Production (units)': [800, 1000, 900, 1200, 700, 600],
        'Rice Production (units)': [1200, 700, 1300, 1000, 800, 500],
        'Wheat Production (units)': [900, 1200, 1100, 1300, 600, 700],
        'Potato Production (units)': [500, 600, 800, 900, 500, 400]}

# Create a dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and ticklabels
if np.random.rand() < 0.7:
    # Set ticks and ticklabels
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0])
    ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
else:
    # Do not set ticks and ticklabels
    ax.set_xticks([])
    ax.set_yticks([])

# Set background grid lines
ax.grid(color='lightgrey', linestyle='--', linewidth=0.5, alpha=0.5)

# Calculate max total value and round up to nearest multiple of 10, 100, or 1000
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5],
              labels=['Corn Production', 'Soybean Production', 'Rice Production', 'Wheat Production', 'Potato Production'],
              colors=['#FFA07A', '#87CEFA', '#90EE90', '#F4A460', '#FFDAB9'], alpha=0.7)

# Set legend position
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Set title
ax.set_title('Crop Production by Region')

# Automatically resize plot to fit legend
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-155112_50.png', bbox_inches='tight')

# Clear plot
plt.clf()