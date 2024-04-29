



# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data
data = {'2021': ['Visual Arts (Exhibitions)', 'Music (Concerts)', 'Performing Arts (Shows)', 'Film (Screenings)', 'Literature (Festivals)'],
        'January': [10, 5, 8, 3, 2],
        'February': [8, 6, 7, 4, 3],
        'March': [12, 7, 9, 5, 3],
        'April': [9, 4, 6, 2, 1],
        'May': [11, 5, 8, 3, 2],
        'June': [10, 6, 7, 4, 3],
        'July': [12, 7, 9, 5, 3],
        'August': [9, 4, 6, 2, 1],
        'September': [11, 5, 8, 3, 2],
        'October': [10, 6, 7, 4, 3],
        'November': [12, 7, 9, 5, 3],
        'December': [9, 4, 6, 2, 1]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max())

# Set y limit and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot the data with area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].values.transpose(), labels=df.columns[1:],
             colors=['#C25255', '#F18F01', '#A1C181', '#6C8EAD', '#BAC7D1', '#FF6347', '#6A5ACD', '#7FFF00', '#32CD32', '#00FFFF', '#A0522D', '#FF4500', '#6495ED'], alpha=0.7)

# Add grid lines
plt.grid(axis='y', linestyle='--')

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# Adjust legend position
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Automatically resize the image
plt.tight_layout()

# Add title
plt.title('Arts and Culture Events by Month in 2021')

# Save the image
plt.savefig('output/final/area_chart/png/20231228-145339_77.png', bbox_inches='tight')

# Clear the current image state
plt.clf()