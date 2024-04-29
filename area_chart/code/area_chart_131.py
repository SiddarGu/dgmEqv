
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Convert data to dictionary
data = {
    'Year': [2018, 2019, 2020, 2021],
    'Total Revenue ($)': [500000, 550000, 600000, 650000],
    'State Revenue ($)': [320000, 350000, 380000, 410000],
    'Federal Revenue ($)': [180000, 200000, 220000, 240000],
    'State Expenditure ($)': [300000, 320000, 340000, 360000],
    'Federal Expenditure ($)': [200000, 230000, 260000, 290000]
}

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10, 6))

# Set axis for the plot
ax = fig.add_axes([0, 0, 1, 1])

# Set background grid lines
ax.grid(True)

# Plot the data as an area chart
ax.stackplot(df['Year'], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns, alpha=0.8)

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max())

# Set y limit and y ticks
ax.set_ylim(0, max_total_value + 50000)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Amount ($)')
ax.set_title('Government Revenue and Expenditure Analysis from 2018 to 2021')

# Set legend
ax.legend(loc='upper left')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/area_chart/png/20231228-140159_45.png', bbox_inches='tight')

# Clear the current image state
plt.clf()