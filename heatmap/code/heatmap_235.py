
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define data
data = {'Category': ['United States', 'Canada', 'United Kingdom', 'Germany', 'Japan'],
        'Healthcare Spending (in billions)': [3.5, 2.9, 2.2, 2.5, 2.0],
        'Life Expectancy (years)': [78, 82, 80, 81, 84],
        'Doctors per 1000 People': [2.5, 2.8, 2.6, 3.0, 2.2],
        'Infant Mortality Rate (per 1000 live births)': [5, 4.5, 4, 4.2, 2.8],
        'Obesity Rate (%)': [35, 25, 30, 27, 23],
        'Vaccination Rate (%)': [80, 85, 90, 85, 95]}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set style of seaborn
sns.set_style("white")

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 5))

# Plot heatmap using seaborn
sns.heatmap(df.drop('Category', axis=1), cmap='Blues', annot=True, fmt='.0f', ax=ax)

# Add title
ax.set_title('Healthcare Comparisons by Country')

# Set ticks and tick labels
ax.set_xticks(np.arange(0.5, len(df.columns)-1, 1))
ax.set_yticks(np.arange(0.5, len(df), 1))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Category'], rotation=0, ha='right', rotation_mode='anchor')

# Set ticks and tick labels in the center of rows and columns
ax.tick_params(axis='x', which='major', pad=10)
ax.tick_params(axis='y', which='major', pad=10)

# Resize image and save
fig.tight_layout()
fig.savefig('output/final/heatmap/png/20231228-155147_24.png', bbox_inches='tight')

# Clear current image state
plt.clf()
plt.close()