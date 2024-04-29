
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Represent the data using a dictionary
data = {'2019': ['Facebook (Users)', 'Instagram (Users)', 'Twitter (Users)', 'LinkedIn (Users)', 'Reddit (Users)'],
        'Q1': [180, 200, 150, 130, 100],
        'Q2': [200, 220, 180, 150, 120],
        'Q3': [220, 240, 200, 170, 140],
        'Q4': [240, 260, 220, 190, 160]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with type of area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns)

# Set x and y axis ticks and labels
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(axis='y', linestyle='--')

# Set legend and labels
ax.legend(loc='upper left')
ax.set_xlabel('Quarter')
ax.set_ylabel('Number of Users')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_90.png', bbox_inches='tight')

# Clear current image state
plt.clf()

# Title of the figure
plt.title('Social Media User Growth by Platform in 2019')

# Show the chart
plt.show()