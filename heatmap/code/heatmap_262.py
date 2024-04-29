
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Import data
data = {'Category': ['Technology', 'Retail', 'Banking', 'Energy', 'Healthcare'],
        'Revenue (in millions)': [500, 400, 600, 700, 800],
        'Expenses (in millions)': [300, 350, 400, 600, 700],
        'Profit (in millions)': [200, 50, 200, 100, 100],
        'Assets (in millions)': [1000, 800, 1200, 1500, 2000],
        'Liabilities (in millions)': [500, 400, 600, 750, 1000]}

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(12, 8))

# Set x and y ticks
x_ticks = np.arange(len(df['Category']))
y_ticks = np.arange(len(df.columns[1:]))

# Set tick labels
x_labels = df['Category']
y_labels = df.columns[1:]

# Plot heatmap using sns.heatmap()
ax = sns.heatmap(df.iloc[:, 1:], annot=True, cmap='coolwarm', cbar=False)

# Set x and y ticks and labels
ax.set_xticks(x_ticks + 0.5)
ax.set_yticks(y_ticks + 0.5)
ax.set_xticklabels(x_labels, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(y_labels, rotation=0, ha='right', rotation_mode='anchor')

# Set axis labels and title
plt.xlabel('Category')
plt.ylabel('Financial Metrics')
plt.title('Financial Performance by Industry')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-162116_16.png', bbox_inches='tight')

# Clear image
plt.clf()