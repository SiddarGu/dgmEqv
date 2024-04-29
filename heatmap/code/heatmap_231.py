
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create data dictionary
data = {'Organization': ['Charity A', 'Charity B', 'Charity C', 'Nonprofit A', 'Nonprofit B'], 
        'Fundraising Revenue ($)': [10, 15, 20, 30, 40], 
        'Grants Received ($)': [100000, 250000, 500000, 125000, 175000], 
        'Donations Received ($)': [1000000, 750000, 500000, 250000, 375000]}

# Convert data dictionary into dataframe
df = pd.DataFrame(data)

# Set figure size and create subplots
fig, ax = plt.subplots(figsize=(10, 8))

# Create heatmap chart using seaborn
import seaborn as sns
sns.heatmap(df.set_index('Organization'), annot=True, cmap='Blues', ax=ax)

# Set ticks and ticklabels for x and y axis
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='center')

# Add title and resize image
plt.title('Financial Performance in Charities and Nonprofits')
plt.tight_layout()

# Save figure as png
plt.savefig('output/final/heatmap/png/20231228-155147_20.png', bbox_inches='tight')

# Clear current image state
plt.clf()