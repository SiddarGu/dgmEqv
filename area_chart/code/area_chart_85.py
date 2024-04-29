
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Represent the data using a dictionary
data = {'2019': ['Q1', 'Q2', 'Q3', 'Q4'], 
        'Electronics Production (Units)': [200000, 250000, 300000, 280000], 
        'Food Production (Units)': [150000, 180000, 200000, 150000], 
        'Pharmaceutical Production (Units)': [180000, 200000, 250000, 220000], 
        'Automotive Production (Units)': [130000, 150000, 180000, 200000]}

# Process the data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figsize parameter
plt.figure(figsize=(12,6))

# Plot the data with the type of area chart
ax = df.plot.area(x='2019', stacked=True, colormap='Set2', alpha=0.7)

# Set x and y axis labels
ax.set_xlabel('Quarter in 2019')
ax.set_ylabel('Production (Units)')

# Set x and y axis ticks and ticklabels
if np.random.randint(0, 10) < 7:
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['2019'])
    ax.set_xlim(0, len(df.index) - 1)

if np.random.randint(0, 10) < 7:
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(axis='y', linestyle='--', alpha=0.3)

# Set title
ax.set_title('Manufacturing Production by Industry and Quarter in 2019')

# Set legend's position
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1.02))

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/area_chart/png/20231228-131755_69.png', bbox_inches='tight')

# Clear the current image state
plt.clf()