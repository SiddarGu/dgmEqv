
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define data
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio'],
        'Truck (unit)': [500, 400, 300, 250, 200, 150, 100],
        'Train (unit)': [200, 150, 100, 90, 80, 60, 50],
        'Ship (unit)': [100, 50, 70, 60, 40, 30, 20],
        'Plane (unit)': [50, 40, 30, 25, 20, 15, 10],
        'Bicycle (unit)': [250, 200, 150, 100, 80, 60, 40],
        'Scooter (unit)': [150, 100, 80, 70, 60, 50, 30]}

# Convert data into dataframe
df = pd.DataFrame(data)

# Set city as index
df = df.set_index('City')

# Set figure size
plt.figure(figsize=(10,8))

# Plot heatmap using seaborn
ax = sns.heatmap(df, annot=True, cbar=True, fmt='g', cmap='Blues')

# Rotate x and y ticks
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(rotation=0)

# Set ticks and tick labels to center
ax.set_xticks([i + 0.5 for i in range(len(df.columns))])
ax.set_yticks([i + 0.5 for i in range(len(df))])
ax.set_xticklabels(df.columns, rotation=45, ha='center')
ax.set_yticklabels(df.index, rotation=0, ha='right')

# Set title
plt.title('Transportation Usage in Major Cities')

# Automatically resize image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-155147_19.png', bbox_inches='tight')

# Clear the current figure
plt.clf()