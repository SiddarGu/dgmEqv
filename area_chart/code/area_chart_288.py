
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {
    'Year': [2016, 2017, 2018, 2019, 2020],
    'Food Sales (Millions of USD)': [2000, 2200, 2500, 2800, 3000],
    'Beverage Sales (Millions of USD)': [1500, 1800, 2000, 2500, 2800]
}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Calculate max total value and set y limits and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot the data as an area chart
ax.stackplot(df['Year'], df['Food Sales (Millions of USD)'], df['Beverage Sales (Millions of USD)'], labels=['Food Sales', 'Beverage Sales'], colors=['#87CEEB', '#FFDAB9'], alpha=0.7)

# Set grid lines
ax.grid(linestyle='--', linewidth=0.5, color='#999999')

# Set legend and title
ax.legend(loc='upper left')
plt.title('Food and Beverage Sales Trends')

# Set x and y labels
ax.set_xlabel('Year')
ax.set_ylabel('Sales (Millions of USD)')

# Automatically resize image
fig.tight_layout()

# Save the chart as a png file
plt.savefig('output/final/area_chart/png/20231228-155112_56.png', bbox_inches='tight')

# Clear current image state
plt.clf()