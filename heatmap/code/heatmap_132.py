
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Convert data to pandas dataframe
data = {'Category': ['United States', 'Europe', 'Asia', 'South America', 'Australia'],
        'Number of Museums': [1500, 1000, 500, 200, 100],
        'Number of Art Galleries': [2000, 1500, 1000, 400, 200],
        'Number of Theaters': [2500, 2000, 1500, 600, 300],
        'Number of Concert Halls': [3000, 2500, 2000, 800, 400],
        'Number of Libraries': [3500, 3000, 2500, 1000, 500]}

df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 8))

# Create heatmap chart using seaborn
ax = sns.heatmap(data=df.set_index('Category'), annot=True, cmap='coolwarm')

# Set x and y ticks and tick labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='right', rotation_mode='anchor')

# Set title
plt.title('Cultural Institutions by Region')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_38.png', bbox_inches='tight')

# Clear image state
plt.clf()