
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set data using a dictionary
data = {'Year': [2019, 2020, 2021, 2022], 
        'Education ($)': [5000, 5200, 4500, 5100], 
        'Healthcare ($)': [4000, 4100, 4900, 3500], 
        'Infrastructure ($)': [6000, 5500, 3300, 3200], 
        'Social Programs ($)': [3000, 2200, 2800, 2500], 
        'Public Safety ($)': [2000, 2500, 3000, 2600]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create subplot
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

# Calculate max total value and set y limit and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x limit and ticks
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])

# Set grid lines
ax.grid(color='lightgrey', linestyle='--')

# Plot stacked area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].values.T, labels=df.columns[1:])

# Set legend and position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title and axis labels
ax.set_title('Government Spending for Public Welfare')
ax.set_xlabel('Year')
ax.set_ylabel('Amount ($)')

# Automatically resize image and save
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-140159_81.png', bbox_inches='tight')

# Clear figure
plt.clf()