
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the data
data = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], 'Furniture (Units)': [1000, 1200, 1400, 1600, 1700, 1800, 2000, 2200, 2400, 2600, 2800, 3000], 'Electronics (Units)': [800, 900, 1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000], 'Clothing (Units)': [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000], 'Automobiles (Units)': [700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250]}

# Convert data into pandas dataframe
df = pd.DataFrame(data)

# Convert the first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data using area chart
fig, ax = plt.subplots(figsize=(14,8)) # Set figure size
ax.stackplot(df['Month'], df.iloc[:, 1:].T, labels=df.iloc[:, 1:].columns, alpha=0.7) # Plot the area chart
ax.legend(loc='upper left') # Set legend location
ax.set_title('Manufacturing and Production Trends by Month') # Set title

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df['Month'])))
ax.set_xticklabels(df['Month'])

# Set yticks and yticklabels
max_total_value = df.iloc[:, 1:].sum(axis=1).max() # Calculate max total value
max_total_value = np.ceil(max_total_value/100)*100 # Round up to the nearest multiple of 100
ytick_num = np.random.choice([3, 5, 7, 9, 11]) # Choose a random number of yticks
yticks = np.linspace(0, max_total_value, ytick_num, dtype=np.int32) # Set yticks
ax.set_yticks(yticks) # Set yticks
ax.set_yticklabels(yticks, rotation=45, rotation_mode='anchor', ha='right') # Set yticklabels

# Set background grid lines
ax.grid(color='lightgrey', linestyle='--')

# Automatically resize the image
fig.tight_layout()

# Save the figure as a png file
fig.savefig('output/final/area_chart/png/20231228-161902_6.png', bbox_inches='tight')

# Clear the current image state
plt.clf()