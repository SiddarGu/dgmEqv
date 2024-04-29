
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create dictionary with data
data = {'Year': [2018, 2019, 2020, 2021, 2022],
        'Revenue ($ billions)': [100, 110, 120, 130, 140],
        'Profit Margin (%)': [15, 16, 17, 18, 19],
        'Operating Expenses ($ billions)': [80, 90, 100, 110, 120],
        'Employees (thousands)': [50, 55, 60, 65, 70]
        }

# Convert dictionary to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(12, 8))

# Create heatmap using seaborn
sns.set(font_scale=1.2)
ax = sns.heatmap(df.set_index('Year'),
                 annot=True,
                 fmt='.0f',
                 cmap='Blues',
                 vmin=0,
                 vmax=150,
                 center=75,
                 linewidths=0.5,
                 linecolor='white',
                 cbar_kws={"shrink": 0.5, "orientation": "horizontal"})

# Set ticks and tick labels for x and y axis
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='right', rotation_mode='anchor')

# Set title
plt.title("Financial and Operational Metrics of Tech Companies")

# Automatically resize image and save figure
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-134212_60.png', bbox_inches='tight')

# Clear current image state
plt.clf()
plt.cla()
plt.close()