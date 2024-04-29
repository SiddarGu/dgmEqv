
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Food Sales ($)': [25000, 23000, 24000, 26000, 25000, 27000, 29000, 30000, 28000, 25000, 24000, 26000],
        'Beverage Sales ($)': [18000, 20000, 22000, 21000, 20000, 22000, 23000, 24000, 22000, 20000, 21000, 22000],
        'Total Sales ($)': [43000, 43000, 46000, 47000, 45000, 49000, 52000, 54000, 50000, 45000, 45000, 48000]}
# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data as an area chart using ax.stackplot()
fig, ax = plt.subplots(figsize=(12, 6)) # Set a larger figsize to prevent content from being displayed
ax.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns, colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.7) # Set colors and transparency
ax.set_title('Food and Beverage Sales by Month') # Set title
ax.set_xlabel('Month') # Set x-axis label
ax.set_ylabel('Total Sales ($)\nFood Sales ($)\nBeverage Sales ($)') # Set y-axis label and move legend unit into it
ax.set_xticks(np.linspace(0, len(df.index) - 1, 12, dtype=np.int32)) # Set x-axis ticks
ax.set_xticklabels(df['Month']) # Set x-axis ticklabels
ax.legend(loc='upper left', bbox_to_anchor=(1, 1)) # Adjust legend position to avoid overlapping with the content
ax.grid(True) # Randomly set background grid lines

# Calculate max total value and set suitable ylim range and yticks
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000 # Calculate max total value and ceil it up to the nearest multiple of 1000
yticks_length = np.random.choice([3, 5, 7, 9, 11]) # Randomly choose the length of yticks
ax.set_ylim(0, max_total_value) # Set ylim range
ax.set_yticks(np.linspace(0, max_total_value, yticks_length, dtype=np.int32)) # Set yticks

# Automatically resize the image by tight_layout() before savefig()
fig.tight_layout()

# Save the figure as a PNG image
plt.savefig('output/final/area_chart/png/20231228-131755_34.png', bbox_inches='tight')

# Clear the current image state
plt.clf()