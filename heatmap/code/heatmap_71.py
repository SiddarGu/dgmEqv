
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data processing
data = {'Country': ['United States', 'China', 'India', 'Brazil', 'Russia', 'France', 'Canada', 'Argentina'], 
        'Crop Yield Index': [100, 90, 80, 85, 75, 95, 80, 90], 
        'Food Export (%)': [20, 15, 10, 25, 30, 15, 20, 25], 
        'Irrigated Land (%)': [80, 65, 70, 40, 10, 50, 30, 15], 
        'Arable Land (%)': [15, 10, 12, 20, 8, 18, 25, 15], 
        'Fertilizer Consumption (kg/ha)': [150, 200, 175, 100, 75, 125, 75, 100]}

df = pd.DataFrame(data)
df = df.set_index('Country')

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df, annot=True, fmt='.0f', cmap='YlGnBu', cbar=True, ax=ax)

# Formatting
ax.set_title('Agricultural Indicators by Country')
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right')
ax.tick_params(axis='x', pad=0)
ax.tick_params(axis='y', pad=0)

# Saving and clearing
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_60.png', bbox_inches='tight')
plt.clf()