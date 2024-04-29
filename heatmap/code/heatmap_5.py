
# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create dictionary with data
data = {'Law Firm': ['Smith & Smith', 'Johnson & Johnson', 'Brown Law', 'Legal Solutions', 'Smith & Jones'],
        'Number of Lawyers': [200, 150, 100, 50, 300],
        'Number of Active Cases': [500, 450, 300, 100, 800],
        'Number of Wins': [400, 300, 200, 80, 600],
        'Number of Losses': [100, 150, 100, 20, 200]}

# Convert dictionary to dataframe
df = pd.DataFrame.from_dict(data)

# Set Law Firm as index for dataframe
df.set_index('Law Firm', inplace=True)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot heatmap using seaborn
sns.heatmap(df[['Number of Lawyers', 'Number of Active Cases', 'Number of Wins', 'Number of Losses']],
            annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax)

# Set axis labels and ticks
ax.set_xlabel('Performance Metrics', fontsize=12)
ax.set_ylabel('Law Firm', fontsize=12)
ax.set_xticklabels(['Number of Lawyers', 'Number of Active Cases', 'Number of Wins', 'Number of Losses'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(['Smith & Smith', 'Johnson & Johnson', 'Brown Law', 'Legal Solutions', 'Smith & Jones'], rotation=0, ha='right', rotation_mode='anchor')

# Add title and resize image
plt.title('Law Firm Performance Metrics', fontsize=14)
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231225-210514_21.png', bbox_inches='tight')

# Clear current image state
plt.clf()