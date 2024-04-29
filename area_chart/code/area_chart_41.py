
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {'Category': ['Government', 'Business', 'Education', 'Non-Profit', 'Healthcare', 'Agriculture', 'Hospitality', 'Retail', 'Construction', 'Transportation', 'Energy', 'Technology', 'Food & Beverage', 'Manufacturing', 'Real Estate'], 
        'Recycling (%)': [50, 40, 30, 20, 10, 15, 25, 35, 45, 55, 65, 75, 85, 90, 100],
        'Energy Usage (%)': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
        'Water Conservation (%)': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],
        'Sustainable Transport (%)': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],
        'Green Spaces (%)': [60, 50, 40, 30, 20, 10, 5, 0, 10, 20, 30, 40, 50, 60, 70]}

# Convert data into pandas dataframe
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set up figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot area chart
ax.stackplot(df.index, df['Recycling (%)'], df['Energy Usage (%)'], df['Water Conservation (%)'], df['Sustainable Transport (%)'], df['Green Spaces (%)'], labels=['Recycling', 'Energy Usage', 'Water Conservation', 'Sustainable Transport', 'Green Spaces'], alpha=0.8)

# Set x and y axis ticks and labels
ax.set_xticks(df.index)
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/10)*10
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_yticklabels([str(i) + '%' for i in ax.get_yticks()])

# Set grid lines
ax.grid(axis='y', alpha=0.5)

# Set legend and title
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.set_title('Environmental Sustainability by Industry')

# Automatically resize image
fig.tight_layout()

# Save image
fig.savefig('output/final/area_chart/png/20231228-131755_12.png', bbox_inches='tight')

# Clear current image state
plt.clf()