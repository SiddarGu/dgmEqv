
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {'Mode':['Truck', 'Train', 'Airplane', 'Ship', 'Pipeline'],
        'Shipping (Packages)':[50000, 10000, 5000, 20000, 1000],
        'Logistics (Packages)':[40000, 20000, 10000, 30000, 5000],
        'Air (Kilometers)':[500000, 300000, 100000, 100000, 10000],
        'Rail (Kilometers)':[300000, 500000, 200000, 200000, 20000],
        'Road (Kilometers)':[700000, 100000, 50000, 400000, 10000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create plot
fig, ax = plt.subplots(figsize=(12, 8))

# Set x and y axis ticks and labels
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/1000)*1000
ax.set_ylim(0, max_total_value)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3,5,7,9,11]), dtype=np.int32))
ax.set_ylabel('Distance (Kilometers)')

# Plot the data as an area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], df.iloc[:, 1],
             labels=['Logistics', 'Air', 'Rail', 'Road', 'Shipping'], alpha=0.7)

# Set background grid lines
ax.grid(axis='y', color='grey', linestyle='--', linewidth=0.5, alpha=0.5)

# Set legend position and title
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)
ax.set_title('Distribution of Transportation Modes and Distances')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_83.png', bbox_inches='tight')

# Clear current image state
plt.clf()