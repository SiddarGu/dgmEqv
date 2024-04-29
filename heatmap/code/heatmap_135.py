
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {'Country': ['United States', 'Canada', 'United Kingdom', 'Germany', 'France', 'Japan'],
        'Tax Revenue (Billions)': [3.5, 2.8, 3.0, 2.5, 3.2, 2.0],
        'Education Spending (Billions)': [5.6, 4.2, 4.8, 3.9, 5.1, 3.2],
        'Healthcare Spending (Billions)': [7.2, 6.5, 6.2, 5.5, 6.8, 4.5],
        'Infrastructure Investment (Billions)': [8.9, 7.8, 7.5, 6.8, 8.2, 5.6],
        'Military Spending (Billions)': [10.1, 8.5, 9.2, 8.0, 9.5, 6.8]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Set size of figure
plt.figure(figsize=(10, 8))

# Set title of figure
plt.title("Government Spending by Country")

# Plot heatmap using seaborn
ax = sns.heatmap(df.drop('Country', axis=1), annot=True, cmap='Blues', cbar=True)

# Set ticks and tick labels for x and y axis
ax.set_xticks(np.arange(5) + 0.5)
ax.set_yticks(np.arange(6) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Country'], rotation=0)

# Resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_43.png', bbox_inches='tight')

# Clear current image state
plt.clf()