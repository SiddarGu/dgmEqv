
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# define data dictionary
data = {'Category': ['IT', 'Marketing', 'Finance', 'Education', 'Healthcare', 'Science', 'Business', 'Government', 'E-commerce', 'Gaming', 'Mobile', 'Retail', 'Telecommunications', 'Automotive'], 'Web Development (Users)': [200, 100, 150, 100, 200, 150, 180, 130, 250, 120, 180, 150, 120, 100], 'Data Science (Users)': [150, 120, 180, 200, 180, 200, 150, 100, 130, 100, 200, 180, 150, 200], 'Cybersecurity (Users)': [180, 150, 200, 250, 150, 100, 100, 150, 100, 200, 150, 130, 200, 250], 'Artificial Intelligence (Users)': [130, 100, 150, 180, 130, 250, 200, 180, 200, 180, 100, 200, 170, 150], 'Social Media (Users)': [250, 200, 250, 150, 100, 120, 170, 200, 150, 150, 250, 100, 130, 180]}

# convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# calculate max total value and set y limit and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# plot stacked area chart
ax.stackplot(df.index, df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.8)

# set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(df.index)
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
    ax.set_xlim(0, len(df.index) - 1)
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_yticklabels(ax.get_yticks(), rotation=45, ha='right', rotation_mode='anchor')

# add background grid lines
ax.grid(axis='y', color='gray', alpha=0.5, linestyle='--')

# set legend and title
ax.legend(loc='upper left')
ax.set_title('User Distribution across Industry Categories')

# automatically resize image and savefig
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231226-130527_0.png', bbox_inches='tight')

# clear image state
plt.clf()
