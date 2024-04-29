
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {'Category': ['Industry', 'Agriculture', 'Transportation', 'Residential', 'Commercial'],
        'Carbon Emissions (kt)': [100, 50, 80, 30, 40],
        'Water Usage (million cubic meters)': [250, 100, 200, 50, 75],
        'Energy Consumption (million kWh)': [500, 200, 400, 100, 150],
        'Waste Generation (million tonnes)': [20, 10, 15, 5, 7],
        'Land Use (thousand hectares)': [100, 50, 75, 25, 35]}

# Convert data into a pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 8))

# Create heatmap using seaborn
sns.heatmap(df.iloc[:, 1:], annot=True, fmt='g', cmap='Blues')

# Set tick labels and rotation
plt.xticks(ticks=np.arange(5)+0.5, labels=df['Category'], rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(ticks=np.arange(5)+0.5, labels=df['Category'], rotation=0)

# Add title and labels
plt.title('Environmental Impact by Industry Type')
plt.xlabel('Environmental Metrics')
plt.ylabel('Industry Type')

# Automatically resize image and save figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_84.png', bbox_inches='tight')

# Clear current image state
plt.clf()