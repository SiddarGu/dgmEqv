
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Process data
data = {'State': ['Texas', 'California', 'New York', 'Florida', 'Illinois'],
        'Primary Care Physicians per 100,000 Population': [75, 80, 85, 70, 65],
        'Specialist Physicians per 100,000 Population': [50, 55, 60, 45, 40],
        'Nurses per 100,000 Population': [200, 190, 180, 210, 220],
        'Hospital Beds per 100,000 Population': [150, 140, 130, 160, 170],
        'Healthcare Expenditure per Capita': [500, 530, 550, 480, 470]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 6))

# Plot heatmap using seaborn
ax = sns.heatmap(df.set_index('State'), annot=True, fmt='.0f', cmap='Blues', cbar=False)

# Set tick positions and labels
ax.set_yticks(np.arange(len(df)) + 0.5)
ax.set_yticklabels(df['State'], rotation=0, ha='right')
ax.set_xticks(np.arange(len(df.columns[1:]))+ 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right')

# Add title
ax.set_title('Healthcare Resources by State')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-134212_12.png', bbox_inches='tight')

# Clear current image state
plt.clf()