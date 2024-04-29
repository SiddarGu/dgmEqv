


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Process the data
data = {'Category': ['Technology', 'Retail', 'Finance', 'Healthcare', 'Energy'],
        'Revenue (Million [ABBREVIATED])': [100, 70, 50, 40, 30],
        'Expenses (Million [ABBREVIATED])': [80, 60, 40, 30, 20],
        'Net Profit (Million [ABBREVIATED])': [20, 10, 10, 10, 10]}

df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(8,6))

# Use seaborn heatmap to plot the chart
ax = sns.heatmap(df.drop('Category', axis=1), annot=True, cmap="YlGnBu", fmt='g')

# Set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(3)+0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(5)+0.5)
ax.set_yticklabels(df['Category'], rotation=0, ha='right', rotation_mode='anchor')

# Set the title of the figure
ax.set_title('Financial Performance by Industry')

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_86.png', bbox_inches='tight')

# Clear the current image state
plt.clf()