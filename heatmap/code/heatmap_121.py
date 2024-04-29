
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {'Country':['France', 'Italy', 'United Kingdom', 'Germany', 'Spain', 'Netherlands', 'Russia'],
        'Theatre':[50, 45, 40, 35, 30, 25, 20],
        'Opera':[40, 35, 30, 25, 20, 15, 10],
        'Concert Hall':[30, 25, 20, 15, 10, 10, 5],
        'Art Gallery':[20, 15, 10, 10, 5, 5, 2],
        'Museum':[10, 10, 5, 5, 2, 2, 1],
        'Architectural Landmarks':[5, 5, 2, 2, 1, 1, 1]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set size of figure
fig, ax = plt.subplots(figsize=(10,8))

# Plot heatmap using seaborn
sns.heatmap(df.drop('Country', axis=1), cmap='Blues', annot=True, fmt='g', ax=ax)

# Set x and y ticklabels
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Country'], rotation=0, ha='right', rotation_mode='anchor')

# Add title and labels
plt.title('Cultural Venues by Country')
plt.xlabel('Venue Type')
plt.ylabel('Country')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-131639_25.png', bbox_inches='tight')

# Clear current state
plt.clf()