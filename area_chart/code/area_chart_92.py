
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Represent data using a dictionary
data = {'Category': ['Q1', 'Q2', 'Q3', 'Q4'],
        'Biology (%)': [20, 25, 30, 25],
        'Chemistry (%)': [20, 25, 25, 30],
        'Physics (%)': [20, 25, 20, 20],
        'Astronomy (%)': [20, 15, 15, 15],
        'Geology (%)': [20, 10, 10, 10]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with an area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(df['Category'], df['Biology (%)'], df['Chemistry (%)'], df['Physics (%)'], df['Astronomy (%)'], df['Geology (%)'], labels=['Biology', 'Chemistry', 'Physics', 'Astronomy', 'Geology'], colors=['#FCD739', '#009CD6', '#0D0D0D', '#FF4A4A', '#2E9A3B'], alpha=0.7)

# Set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
if np.random.choice([True, False], p=[0.7, 0.3]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 100) * 100
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(axis='y', linestyle='--')

# Set legend position and title
ax.legend(loc='upper left', title='Science and Engineering Trends')

# Automatically resize the image and save the figure
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_77.png', bbox_inches='tight')

# Clear the current image state
plt.clf()