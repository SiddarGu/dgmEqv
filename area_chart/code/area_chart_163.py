
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Year': [2016, 2017, 2018, 2019, 2020],
        'Productivity (units)': [200, 220, 230, 240, 250],
        'Waste (units)': [20, 15, 25, 30, 10],
        'Efficiency (%)': [80, 85, 75, 70, 90],
        'Quality (%)': [90, 95, 90, 85, 80]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value and set y limit and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/10) * 10
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df['Year'], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns.tolist(), colors=['#4BACC6', '#F79646', '#9BBB59', '#8064A2'], alpha=0.8)

# Set grid lines
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)

# Set ticks and ticklabels for x axis
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')

# Set title and labels
ax.set_title('Manufacturing and Production Trends', fontsize=16)
ax.set_xlabel('Year')
ax.set_ylabel('Units')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_83.png', bbox_inches='tight')

# Clear current image state
plt.clf()