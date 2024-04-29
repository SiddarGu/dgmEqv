
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data as a dictionary
data = {'Department': ['Administration', 'Sales', 'IT', 'HR', 'R&D'],
       'Finance': [200, 280, 270, 150, 180],
       'Marketing': [180, 300, 250, 160, 200],
       'Operations': [220, 320, 230, 170, 210],
       'Human Resources': [210, 310, 240, 180, 190],
       'Research & Development': [250, 290, 260, 190, 230]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize=(10,6))

# Set the title of the figure
ax.set_title('Employee Distribution by Department')

# Calculate the max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Ceil max_total_value up to the nearest multiple of 10, 100 or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value/10)*10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value/100)*100
else:
    max_total_value = np.ceil(max_total_value/1000)*1000

# Set y lim range
ax.set_ylim(0, max_total_value)

# Set x ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor', wrap=True)

# Set y ticks and ticklabels
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(True, color='lightgrey', alpha=0.5)

# Plot the data as an area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].values.T, labels=df.columns[1:], alpha=0.8)

# Set legend position
ax.legend(loc='upper left')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/area_chart/png/20231228-155112_5.png', bbox_inches='tight')

# Clear the current image state
plt.clf()