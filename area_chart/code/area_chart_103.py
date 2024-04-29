
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Convert data to dictionary
data = {
    'Category': ['Asia', 'Europe', 'North America', 'South America', 'Africa'],
    'Grains (tons)': [50000, 40000, 45000, 30000, 25000],
    'Vegetables (tons)': [30000, 35000, 40000, 20000, 15000],
    'Fruits (tons)': [25000, 30000, 35000, 15000, 10000],
    'Meat (tons)': [20000, 25000, 30000, 10000, 5000],
    'Dairy (tons)': [10000, 15000, 20000, 5000, 2500]
}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot area chart
ax.stackplot(df['Category'], df['Grains (tons)'], df['Vegetables (tons)'], df['Fruits (tons)'], df['Meat (tons)'], df['Dairy (tons)'], labels=['Grains', 'Vegetables', 'Fruits', 'Meat', 'Dairy'], alpha=0.5)

# Set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Category'])
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_yticks(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max()), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.2)

# Adjust legend position
ax.legend(loc='best')

# Set title
ax.set_title('Agricultural Production by Region')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-131755_95.png', bbox_inches='tight')

# Clear figure
plt.clf()