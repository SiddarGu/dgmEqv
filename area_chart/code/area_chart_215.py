
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define the data as a dictionary
data = {'Category': ['Agriculture', 'Transportation', 'Education', 'Healthcare', 'Energy', 'Law Enforcement', 'Housing', 'Environment', 'Defense', 'Welfare', 'Foreign Affairs', 'Infrastructure', 'Social Services', 'Trade', 'Labor'], 'Government Spending ($)': [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000], 'Public Infrastructure ($)': [6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000], 'Social Programs ($)': [4500, 5500, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create axes
fig, ax = plt.subplots(figsize=(12,8))

# Stack the data and plot as an area chart
ax.stackplot(df['Category'], df['Government Spending ($)'], df['Public Infrastructure ($)'], df['Social Programs ($)'], labels=['Government Spending ($)', 'Public Infrastructure ($)', 'Social Programs ($)'])

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)

# Set y ticks
yticks = np.random.choice([3, 5, 7, 9, 11])
ax.set_yticks(np.linspace(0, max_total_value, yticks, dtype=np.int32))
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# Set x and y axis labels
ax.set_xlabel('Category')
ax.set_ylabel('Spending ($)')

# Set grid lines
ax.grid(linestyle='dotted')

# Set legend
ax.legend(loc='upper left')

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_53.png', bbox_inches='tight')

# Close current image state
plt.close('all')

# Show plot
plt.show()

# Clear figure
plt.clf()

# Set title
plt.title('Government Spending on Public Policy Areas')

# Show plot
plt.show()