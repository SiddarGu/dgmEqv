
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Convert data to dictionary and process with pandas
data = {'Year': [2016, 2017, 2018, 2019, 2020],
        'Legislation Passed': [50, 55, 60, 65, 70],
        'Public Opinion (Support)': [60, 70, 65, 75, 80],
        'Public Opinion (Opposition)': [40, 30, 35, 25, 20]}

df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value and set y-axis ticks and labels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Plot the data as an area chart
ax.stackplot(df['Year'], df['Legislation Passed'], df['Public Opinion (Support)'], df['Public Opinion (Opposition)'], labels=['Legislation Passed', 'Public Opinion (Support)', 'Public Opinion (Opposition)'], colors=['#78D5E3', '#7FACD6', '#E88471'], alpha=0.7)

# Set x-axis limits and labels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(range(len(df['Year'])))
ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')

# Set grid lines
ax.grid(color='#AAAAAA', linestyle='--')

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Government Legislation and Public Opinion Analysis')

# Automatically resize image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_90.png', bbox_inches='tight')

# Clear current image state
plt.clf()