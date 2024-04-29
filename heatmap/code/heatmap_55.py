
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import data
data = {'Country': ['United States', 'Canada', 'United Kingdom', 'Germany', 'Japan', 'China', 'India', 'Brazil'],
        'Doctors per 1000 People': [2.5, 2.1, 2.8, 3.3, 2.0, 1.5, 1.0, 1.7],
        'Nurses per 1000 People': [6.3, 4.8, 5.6, 5.2, 4.7, 2.9, 1.8, 3.5],
        'Pharmacists per 1000 People': [1.2, 1.0, 1.3, 1.5, 1.0, 0.8, 0.6, 0.8],
        'Hospital Beds per 1000 People': [2.9, 3.1, 3.5, 3.8, 3.2, 2.1, 1.9, 2.5],
        'Life Expectancy (years)': [78.9, 82.2, 81.4, 81.0, 84.6, 76.1, 69.8, 74.2]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10,8))

# Plot heatmap using seaborn
sns.heatmap(data=df.set_index('Country'), cmap='YlGnBu', annot=True, fmt='.1f', linewidths=0.5, linecolor='white', cbar=False)

# Set ticks and ticklabels for x and y axis
plt.xticks(np.arange(0.5, 5.5), labels=['Doctors', 'Nurses', 'Pharmacists', 'Hospital Beds', 'Life Expectancy'], rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(0.5, 8.5), labels=df['Country'], va='center', rotation=0)

# Set title
plt.title('Healthcare Workforce and Life Expectancy by Country')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-124154_42.png', bbox_inches='tight')

# Clear current image state
plt.clf()