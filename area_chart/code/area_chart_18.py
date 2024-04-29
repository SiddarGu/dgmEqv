
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define data as a dictionary
data = {'Year': [2019, 2020, 2021, 2022], 'Revenue (Million $)': [100, 110, 115, 120], 'Expenses (Million $)': [80, 90, 95, 100], 'Profit (Million $)': [20, 20, 20, 20]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data as an area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(df['Year'], df['Revenue (Million $)'], df['Expenses (Million $)'], df['Profit (Million $)'], labels=['Revenue', 'Expenses', 'Profit'], colors=['#f4d03f', '#e74c3c', '#2ecc71'], alpha=0.7)

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)

# Set y ticks and ticklabels
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, rotation=45, ha='right', rotation_mode='anchor')

# Set x and y axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Million $')

# Set background grid lines
ax.grid(color='#95a5a6', linestyle='--', linewidth=1, alpha=0.2)

# Set legend and legend title
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left', title='Financial Performance')

# Set title
plt.title('Financial Performance from 2019 to 2022')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-103019_28.png', bbox_inches='tight')

# Clear current image state
plt.clf()