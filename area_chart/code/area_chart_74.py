
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Define data as dictionary
data = {'Type': ['Social Media', 'E-commerce', 'Gaming', 'Streaming', 'Search Engines', 'Online Education', 'Online Banking', 'Cloud Computing', 'Digital Advertising', 'Cybersecurity', 'Virtual Reality'], 
        'Internet Users': [600, 350, 200, 300, 500, 250, 400, 300, 450, 350, 150],
        'Mobile Users': [400, 300, 150, 280, 350, 200, 350, 250, 400, 300, 100],
        'Desktop Users': [550, 250, 180, 320, 450, 300, 300, 350, 350, 250, 120]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 6))

# Set x and y axis ticks and tick labels
ax = plt.subplot(111)
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks)
ax.tick_params(axis='both', which='major', labelsize=8)

# Plot the data with area chart
plt.stackplot(df['Type'], df['Internet Users'], df['Mobile Users'], df['Desktop Users'], labels=['Internet Users', 'Mobile Users', 'Desktop Users'], colors=['#ff7f0e', '#1f77b4', '#2ca02c'], alpha=0.7)

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.3)

# Set legend and legend position
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Unit')

# Set title and labels
plt.title('Technology Usage and Adoption Trends')
plt.xlabel('Type')
plt.ylabel('Number of Users')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-131755_57.png', bbox_inches='tight')

# Clear current image state
plt.clf()