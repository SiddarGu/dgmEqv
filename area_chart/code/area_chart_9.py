
# Import required libraries

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define the data as a dictionary

data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Hotel Occupancy Rate (%)': [70, 65, 75, 80, 85], 'Airbnb Occupancy Rate (%)': [60, 70, 75, 80, 85], 'Vacation Rental Occupancy Rate (%)': [50, 55, 65, 70, 75]}

# Convert the data to a dataframe

df = pd.DataFrame(data)

# Convert first column to string type

df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size and create a subplot

fig, ax = plt.subplots(figsize=(12,8))

# Set the max total value for the y axis

max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10.0) * 10.0

# Set the y limits and ticks

ax.set_ylim(0, max_total_value)

ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set the x limits and ticks

ax.set_xlim(0, len(df.index) - 1)

ax.set_xticks(np.arange(len(df.index)))

# Set the x and y labels

ax.set_xlabel('Month')
ax.set_ylabel('Occupancy Rate (%)')

# Plot the data as an area chart

ax.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=['#F2B705', '#E7343F', '#4F81BD'], alpha=0.5)

# Add grid lines

ax.grid(ls='--', alpha=0.3)

# Set the legend position and title

ax.legend(loc='upper right', title='Accommodation Type')

# Set the title of the figure

plt.suptitle('Monthly Accommodation Occupancy Rates')

# Automatically resize the image and save it

plt.tight_layout()

fig.savefig('output/final/area_chart/png/20231226-103019_17.png', bbox_inches='tight')

# Clear the current image state

plt.clf()