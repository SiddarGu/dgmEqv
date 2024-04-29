
# Import required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {'Year': [2019, 2020, 2021, 2022, 2023], 
        'Hotel Rooms (Available)': [1000, 950, 900, 850, 800],
        'Airbnb Listings (Available)': [1200, 1100, 1000, 900, 800],
        'Vacation Rentals (Available)': [500, 550, 600, 650, 700],
        'Hostels (Available)': [200, 250, 300, 350, 400],
        'Bed & Breakfast (Available)': [100, 120, 130, 140, 150]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create subplots
fig, ax = plt.subplots(figsize=(10,6))

# Plot area chart
ax.stackplot(df['Year'], df['Hotel Rooms (Available)'], df['Airbnb Listings (Available)'], df['Vacation Rentals (Available)'], df['Hostels (Available)'], df['Bed & Breakfast (Available)'], labels=['Hotel Rooms', 'Airbnb Listings', 'Vacation Rentals', 'Hostels', 'Bed & Breakfast'], colors=['#253494', '#41b6c4', '#a1dab4', '#fed976', '#e31a1c'], alpha=0.8)

# Set x and y-axis ticks and labels
ax.set_xticks(df.index)
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and set suitable y-axis ticks and range
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value <= 100:
    yticks = [0, 50, 100]
else:
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_ylim(0, max_total_value)
ax.set_yticks(yticks)

# Set background grid lines
ax.grid(axis='y', linestyle='--', linewidth=0.5)

# Set legend and its position
handles, labels = ax.get_legend_handles_labels()
ax.legend(reversed(handles), reversed(labels), loc='upper left')

# Set title and labels
ax.set_title('Available Accommodations by Type from 2019 to 2023')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Available Accommodations')

# Automatically resize image and save as png
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_1.png', bbox_inches='tight')

# Clear current image state
plt.clf()