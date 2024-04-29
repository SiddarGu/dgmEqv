
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Define data as dictionary
data = {'Category': ['Technology', 'Fashion', 'Food', 'Travel', 'Entertainment', 'Art', 'Business', 'Government', 'Fitness', 'Music', 'Beauty', 'Media', 'Education', 'Health'],
        'Facebook (Users)': [200, 100, 150, 100, 200, 150, 180, 130, 250, 120, 180, 150, 120, 100],
        'Twitter (Users)': [150, 120, 180, 200, 180, 200, 150, 100, 130, 100, 200, 180, 150, 200],
        'Instagram (Users)': [180, 150, 200, 250, 150, 100, 100, 150, 100, 200, 150, 130, 200, 250],
        'LinkedIn (Users)': [130, 100, 150, 180, 130, 250, 200, 180, 200, 180, 100, 200, 170, 150],
        'Snapchat (Users)': [250, 200, 250, 150, 100, 120, 170, 200, 150, 150, 250, 100, 130, 180]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value and set y limit
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)

# Set x and y ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot stacked area chart
ax.stackplot(df['Category'], df['Facebook (Users)'], df['Twitter (Users)'], df['Instagram (Users)'], df['LinkedIn (Users)'], df['Snapchat (Users)'],
             labels=['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'Snapchat'], colors=['#3b5998', '#1da1f2', '#e4405f', '#0077b5', '#fffc00'], alpha=0.7)

# Set grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5)

# Set legend and legend placement
legend = ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0, frameon=False)

# Set labels and title
ax.set_xlabel('Category')
ax.set_ylabel('Number of Users')
ax.set_title('Social Media Usage Across Different Industries')

# Automatically resize the image
plt.tight_layout()

# Save and clear figure
plt.savefig('output/final/area_chart/png/20231228-131755_27.png', bbox_inches='tight')
plt.clf()