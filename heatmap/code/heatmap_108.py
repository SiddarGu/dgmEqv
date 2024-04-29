

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set data
country = ['United States', 'China', 'India', 'Brazil', 'Argentina', 'Russia', 'France', 'Canada', 'Germany', 'United Kingdom']
wheat = [3.2, 2.8, 3.5, 4.0, 1.8, 3.1, 2.5, 3.0, 2.7, 2.8]
corn = [5.5, 4.8, 5.2, 6.0, 2.5, 4.0, 3.8, 4.5, 4.0, 4.2]
rice = [3.0, 3.2, 2.7, 6.5, 2.2, 3.6, 3.1, 3.3, 3.2, 3.5]
soybeans = [2.5, 2.7, 2.2, 3.0, 1.5, 2.8, 2.6, 2.9, 2.6, 2.9]
barley = [4.0, 3.5, 3.0, 5.5, 2.0, 4.2, 3.2, 3.8, 3.5, 3.6]
potatoes = [6.1, 5.0, 4.8, 7.2, 3.5, 5.0, 4.6, 5.2, 4.8, 5.1]

# Create dataframe
df = pd.DataFrame({'Country': country, 'Wheat (Tonnes per Hectare)': wheat, 'Corn (Tonnes per Hectare)': corn, 'Rice (Tonnes per Hectare)': rice, 'Soybeans (Tonnes per Hectare)': soybeans, 'Barley (Tonnes per Hectare)': barley, 'Potatoes (Tonnes per Hectare)': potatoes})

# Set figure size
plt.rcParams["figure.figsize"] = (12,10)

# Create heatmap chart
ax = sns.heatmap(df.set_index('Country'), cmap='coolwarm', annot=True, fmt='.1f', linewidths=0.5)

# Set axis ticks and labels
ax.set_xticks(np.arange(0,6)+0.5)
ax.set_xticklabels(['Wheat', 'Corn', 'Rice', 'Soybeans', 'Barley', 'Potatoes'], fontsize=12, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(0,10)+0.5)
ax.set_yticklabels(country, fontsize=12, rotation=0)

# Set tick marks
ax.tick_params(axis='both', which='both', length=0)

# Set title and labels
ax.set_title('Crop Yields by Country in Agriculture', fontsize=16)
ax.set_xlabel('Type of Crop', fontsize=14)
ax.set_ylabel('Country', fontsize=14)

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-130949_5.png', bbox_inches='tight')

# Clear image state
plt.clf()