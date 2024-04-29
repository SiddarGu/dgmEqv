
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create dictionary to store data
data = {
    'Research Topic': ['Humanities', 'Psychology', 'Sociology', 'Economics', 'Political Science'],
    'Linguistics': [15, 20, 25, 30, 10],
    'History': [30, 25, 20, 15, 10],
    'Anthropology': [20, 25, 25, 15, 15],
    'Communications': [25, 20, 20, 20, 15],
    'Philosophy': [10, 20, 25, 30, 15]
}


# Convert data to pandas dataframe
df = pd.DataFrame.from_dict(data)

# Create heatmap chart using seaborn
sns.set(font_scale=1.2)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df.set_index('Research Topic'), ax=ax, annot=True, cmap='Blues', linewidths=0.5, cbar=False)

# Set ticks and ticklabels for x and y axis
# plt.xticks(np.arange(5) + 0.5, df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
# plt.yticks(np.arange(9) + 0.5, df['Research Topic'], wrap=True, rotation=0, ha='right', rotation_mode='anchor')

# Set title of the figure
plt.title('Research Fields in Social Sciences and Humanities')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_98.png', bbox_inches='tight')

# Clear the current image state
plt.clf()