
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Category': ['Northeast', 'Midwest', 'South', 'West'], 
        'Single Family Home Prices (in thousands)': [450, 300, 400, 500], 
        'Apartment Rental Prices (in thousands)': [250, 200, 300, 350], 
        'Housing Starts': [200, 180, 250, 300], 
        'Home Sales': [300, 250, 350, 400]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data as an area chart
ax.stackplot(df.index, df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=['#F94144','#F3722C','#F8961E','#F9C74F','#90BE6D'], alpha=0.7)

# Set x-axis ticks and labels
ax.set_xticks(df.index)
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Set y-axis ticks and labels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
y_ticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticks)

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, np.ceil(max_total_value / 1000) * 1000)

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.2, alpha=0.5)

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Real Estate Trends by Region')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-155112_30.png', bbox_inches='tight')

# Clear the current image state
plt.clf()