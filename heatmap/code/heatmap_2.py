
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Indicator': ['Doctors per 1000 people', 'Nurses per 1000 people', 'Beds per 1000 people', 'Healthcare Spending per capita', 'Life Expectancy (years)', 'Infant Mortality Rate (deaths per 1000 births)'],
        'United States': [2.5, 2.9, 2.8, 10000, 76, 5],
        'Canada': [2.3, 3.1, 3.2, 9000, 80, 4],
        'United Kingdom': [2.0, 3.5, 3.0, 8000, 81, 3],
        'Germany': [3.0, 3.2, 4.0, 10500, 83, 3],
        'Japan': [2.7, 3.0, 3.8, 9500, 85, 2]}

# Convert data to a dataframe
df = pd.DataFrame(data)

# Set country as index
df.set_index('Indicator', inplace=True)

# Transpose dataframe
df = df.T

# Set figure size
fig = plt.figure(figsize=(10, 8))

# Create heatmap using sns.heatmap()
import seaborn as sns
sns.heatmap(df, cmap='Blues', annot=True, fmt='.0f')

# Add labels and title
plt.xlabel('Healthcare Indicators by Country', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.title('Healthcare Indicators by Country', fontsize=14)

# Set ticks and ticklabels for x and y axis
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(rotation=0, ha='center')

# Automatically resize image and save figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231225-210514_12.png', bbox_inches='tight')

# Clear current image state
plt.clf()