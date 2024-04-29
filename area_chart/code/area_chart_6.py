
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Year': [2016, 2017, 2018, 2019, 2020],
        'Revenue ($)': [100000, 105000, 110000, 120000, 130000],
        'Expenses ($)': [70000, 75000, 80000, 85000, 90000],
        'Profit ($)': [30000, 30000, 30000, 35000, 40000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set x and y axis ticks and ticklabels
ax.set_xticks(np.arange(len(df)))
ax.set_xticklabels(df['Year'])
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and set suitable yticks and ylim range
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_ylim(0, max_total_value)

# Set background grid lines
ax.grid(color='lightgrey', linestyle='dashed')

# Plot area chart
ax.stackplot(df['Year'], df['Revenue ($)'], df['Expenses ($)'], df['Profit ($)'], labels=['Revenue', 'Expenses', 'Profit'], colors=['lightblue', 'lightcoral', 'lightgreen'], alpha=0.7)

# Add legend and adjust position
ax.legend(loc='upper left')
plt.legend(bbox_to_anchor=(1.02, 0.5), loc='center left')

# Automatically resize image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-103019_14.png', bbox_inches='tight')

# Clear current image state
plt.clf()

# Set title
plt.title('Financial Performance from 2016 to 2020')

# Show chart
plt.show()