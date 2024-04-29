
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {'Year': [2019, 2020, 2021, 2022, 2023],
        'Cost ($)': [150000, 160000, 170000, 180000, 190000],
        'Rent ($)': [2000, 2500, 3000, 3500, 4000],
        'Average Price ($)': [300000, 350000, 400000, 450000, 500000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create axes object
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Year'])

# Set yticks
ax.set_yticks(np.linspace(0, ax.get_ylim()[1], np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Cost ($)/Rent ($)/Average Price ($)')

# Plot the data with the type of area chart
ax.stackplot(df.index, df['Cost ($)'], df['Rent ($)'], df['Average Price ($)'], labels=['Cost ($)', 'Rent ($)', 'Average Price ($)'], colors=['#FFB6C1', '#90EE90', '#ADD8E6'], alpha=0.7)

# Set background grid lines
ax.grid(color='gray', linestyle='--')

# Set legend and its position
ax.legend(loc='upper left')

# Automatically resize the image
plt.tight_layout()

# Set title
plt.suptitle('Real Estate Market Trends')

# Save the chart as a png file
plt.savefig('output/final/area_chart/png/20231226-130527_1.png', bbox_inches='tight')

# Clear the current image state
plt.clf()