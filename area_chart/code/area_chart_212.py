
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary with the given data
data = {'Category': ['USA', 'China', 'India', 'Brazil', 'Russia'], 
        'Corn Production (in 1000 tons)': [150, 250, 200, 180, 130], 
        'Soybean Production (in 1000 tons)': [200, 180, 170, 150, 180], 
        'Wheat Production (in 1000 tons)': [180, 150, 220, 200, 150], 
        'Rice Production (in 1000 tons)': [250, 200, 150, 130, 200], 
        'Potato Production (in 1000 tons)': [100, 120, 100, 150, 170]}

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig = plt.figure(figsize=(12, 8))

# Create a new subplot
ax = fig.add_subplot(111)

# Calculate the max total value for the y-axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up to the nearest multiple of 10, 100 or 1000
max_total_value = np.ceil(max_total_value / 10) * 10

# Set the y-axis limit
ax.set_ylim(0, max_total_value)

# Set the y-axis ticks
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set the x-axis limit
ax.set_xlim(0, len(df.index) - 1)

# Create a stackplot
ax.stackplot(df['Category'], df.drop('Category', axis=1).T, labels=df.columns[1:])

# Set the background grid lines
ax.grid(linestyle='dotted')

# Set the legend position
ax.legend(loc='upper left')

# Set the x-axis label
ax.set_xlabel('Country', fontsize=12)

# Set the y-axis label
ax.set_ylabel('Production (in 1000 tons)', fontsize=12)

# Automatically resize the image
fig.tight_layout()

# Set the title
fig.suptitle('Crop Production by Country', fontsize=16)

# Save the figure
fig.savefig('output/final/area_chart/png/20231228-145339_5.png', bbox_inches='tight')

# Clear the current image state
plt.clf()