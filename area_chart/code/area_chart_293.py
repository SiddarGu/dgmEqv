
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data
data = {'Category': ['Sustainable Practices in Manufacturing', 'Agriculture', 'Transportation', 'Construction', 'Energy', 'Retail', 'Hospitality', 'Technology', 'Healthcare', 'Education', 'Government', 'Finance', 'Non-profit', 'Real Estate'], 'Emissions (tonnes)': [5000, 2500, 4000, 3000, 6000, 3500, 2000, 4500, 3000, 2500, 4000, 3500, 2000, 3000], 'Renewable Energy (MWh)': [2000, 3000, 1000, 1500, 4000, 2500, 1000, 3500, 500, 2000, 3000, 2500, 1000, 500], 'Water Usage (gallons)': [10000, 5000, 8000, 2000, 15000, 6000, 3000, 10000, 2000, 5000, 8000, 6000, 3000, 2000], 'Waste (tons)': [500, 200, 300, 400, 1000, 500, 150, 600, 200, 300, 600, 500, 200, 300], 'Sustainable Practices': [75, 50, 60, 70, 80, 90, 40, 100, 30, 20, 50, 70, 10, 40]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data with the type of area chart
ax.stackplot(df['Category'], df['Emissions (tonnes)'], df['Renewable Energy (MWh)'], df['Water Usage (gallons)'], df['Waste (tons)'], df['Sustainable Practices'], colors=['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728', '#9467bd'], alpha=0.7)

# Set x and y axis ticks and ticklabels
ax.set_xticks(range(len(df.index)))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Calculate max total value and set y axis range
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value > 1000:
    max_total_value = np.ceil(max_total_value/1000)*1000
elif max_total_value > 100:
    max_total_value = np.ceil(max_total_value/100)*100
else:
    max_total_value = np.ceil(max_total_value/10)*10

# Set y axis ticks and ticklabels
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_yticklabels(ax.get_yticks(), rotation=0, ha='right', rotation_mode='anchor')

# Set legend
ax.legend(['Emissions (tonnes)', 'Renewable Energy (MWh)', 'Water Usage (gallons)', 'Waste (tons)', 'Sustainable Practices'], loc='upper left', bbox_to_anchor=(1, 1))

# Set title
ax.set_title('Environmental Impact by Industry Category')

# Set background grid lines
ax.grid(color='grey', linestyle='--')

# Automatically resize the image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-155112_9.png', bbox_inches='tight')

# Clear current image state
plt.close(fig)