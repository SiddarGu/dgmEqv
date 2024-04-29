
# import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create a dictionary with the given data
data = {'Year': [2019, 2020, 2021, 2022, 2023],
        'Administration (Employees)': [200, 180, 220, 210, 250],
        'Sales (Employees)': [280, 300, 320, 310, 290],
        'IT (Employees)': [270, 250, 230, 240, 260],
        'HR (Employees)': [150, 160, 170, 180, 190],
        'R&D (Employees)': [180, 200, 210, 190, 230]}

# convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# plot the data using an area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df['Year'], df['Administration (Employees)'],
             df['Sales (Employees)'], df['IT (Employees)'],
             df['HR (Employees)'], df['R&D (Employees)'],
             labels=['Administration', 'Sales', 'IT', 'HR', 'R&D'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
             alpha=0.8)
ax.set_title('Employee Distribution by Department from 2019 to 2023')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Employees')
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')

# calculate max total value and set y-axis ticks and ticklabels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]),
                      dtype=np.int32)
ax.set_ylim(0, max_total_value)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks)

# add background grid lines
ax.grid(linestyle='dotted')

# adjust legend position and add unit to y-axis label
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=5)
ax.set_ylabel('Number of Employees (thousands)')

# resize image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-155112_15.png', bbox_inches='tight')

# clear current image state
plt.clf()