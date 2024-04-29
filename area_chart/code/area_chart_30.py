
# Initialize libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary with data
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Baseball (Revenue)': [100000, 110000, 120000, 130000, 140000],
        'Basketball (Revenue)': [120000, 140000, 150000, 160000, 170000],
        'Football (Revenue)': [150000, 160000, 170000, 180000, 190000],
        'Soccer (Revenue)': [80000, 100000, 120000, 130000, 140000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data as an area chart
ax.stackplot(df['Year'], df['Baseball (Revenue)'], df['Basketball (Revenue)'], df['Football (Revenue)'], df['Soccer (Revenue)'],
             labels=['Baseball', 'Basketball', 'Football', 'Soccer'],
             colors=['#D9E6E8', '#A4C8D4', '#6EA5C4', '#4989B8'],
             alpha=0.8)

# Set x and y axis ticks and tick labels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(ls='--')

# Set legend and place it outside of the plot
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)

# Set title
plt.title('Revenue Comparison among Major Sports Leagues')

# Automatically resize image and save it
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231226-130527_15.png', bbox_inches='tight')

# Clear image state
plt.clf()