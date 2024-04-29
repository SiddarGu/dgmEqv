



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'Category': ['Entertainment', 'News', 'Lifestyle', 'Travel', 'Technology', 'Sports', 'Food', 'Fashion', 'Politics', 'Beauty', 'Health', 'Business'], 
        'Facebook (Users)': [100, 150, 200, 120, 180, 150, 120, 100, 180, 150, 200, 120], 
        'Instagram (Users)': [200, 180, 150, 100, 200, 180, 150, 200, 200, 180, 150, 100], 
        'Twitter (Users)': [150, 200, 180, 150, 150, 130, 200, 250, 150, 200, 180, 150], 
        'YouTube (Users)': [250, 120, 190, 200, 100, 200, 170, 150, 100, 120, 190, 200], 
        'LinkedIn (Users)': [180, 100, 130, 170, 250, 100, 130, 180, 250, 100, 130, 170]}

# Create dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data with area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=['Facebook', 'Instagram', 'Twitter', 'YouTube', 'LinkedIn'], colors=['#3b5998', '#8a3ab9', '#1da1f2', '#ff0000', '#0077b5'], alpha=0.5)

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Ceil max total value up to the nearest multiple of 10, 100 or 1000
if max_total_value < 100:
    max_total_value = 100
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y axis ticks and ticklabels
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_yticklabels(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(alpha=0.3)

# Set legend
ax.legend(loc='upper right')

# Adjust legend's position
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Set title
plt.title('User Distribution by Social Media and Web Category')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_82.png', bbox_inches='tight')

# Clear current image state
plt.clf()