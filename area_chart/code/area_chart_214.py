


# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary with data
data = {'Category': ['Biology', 'Chemistry', 'Physics', 'Engineering'],
        'Research ($)': [20000, 25000, 30000, 35000],
        'Development ($)': [15000, 18000, 20000, 25000],
        'Experimentation ($)': [12000, 15000, 18000, 20000],
        'Testing ($)': [10000, 13000, 15000, 18000],
        'Production ($)': [8000, 10000, 12000, 15000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data with area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.columns[1:], colors=['#7DB3D1', '#9DD1E6', '#F6A6B2', '#FFD8B7', '#FFFCB7'], alpha=0.8)

# Add grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set x and y axis ticks and labels
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df.iloc[:, 0])

# Set y axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y axis labels
ax.set_xlabel('Category')
ax.set_ylabel('Expenditure ($)')
ax.set_title('Science and Engineering Expenditure by Category')

# Move legend to upper left corner
ax.legend(loc='upper left')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_52.png', bbox_inches='tight')

# Clear figure
plt.clf()