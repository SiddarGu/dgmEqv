
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary to store the data
data = {'Type of Accommodation': ['3 Star', '4 Star', '5 Star'],
        'Hotels (Available)': [50, 60, 40],
        'Resorts (Available)': [30, 40, 50],
        'Bed and Breakfast (Available)': [40, 30, 60],
        'Vacation Rentals (Available)': [20, 50, 30],
        'Hostels (Available)': [20, 20, 20]}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Set the x and y axis ticks
ax.set_xticks(np.arange(len(df.index)))
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set the x and y axis tick labels
ax.set_xticklabels(df['Type of Accommodation'])

# Set the x and y axis labels
ax.set_xlabel('Type of Accommodation')
ax.set_ylabel('Number of Available Accommodations')

# Set the title of the figure
ax.set_title('Accommodation Availability by Type')

# Plot the data as an area chart
ax.stackplot(df['Type of Accommodation'], df['Hotels (Available)'], df['Resorts (Available)'], df['Bed and Breakfast (Available)'], df['Vacation Rentals (Available)'], df['Hostels (Available)'], labels=['Hotels', 'Resorts', 'Bed and Breakfast', 'Vacation Rentals', 'Hostels'])

# Add a legend
ax.legend(loc='upper left')

# Set the background grid lines
ax.grid(color='grey', linestyle='dashed', linewidth=0.5)

# Automatically resize the image
fig.tight_layout()

# Save the figure
fig.savefig('output/final/area_chart/png/20231228-131755_68.png', bbox_inches='tight')

# Clear the current image state
plt.clf()