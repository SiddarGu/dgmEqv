
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# convert data to dictionary
data = {'Category': ['Technology', 'Entertainment', 'Fashion', 'Food', 'Travel', 'Beauty', 'Fitness', 'Lifestyle', 'Sports', 'News', 'Music', 'Art', 'Business', 'Health', 'Education', 'Politics', 'Marketing'],
        'Facebook (Users)': [200, 100, 150, 100, 200, 150, 180, 130, 250, 120, 180, 150, 120, 100, 200, 150, 180],
        'Twitter (Users)': [150, 120, 180, 200, 180, 200, 150, 100, 130, 100, 200, 180, 150, 200, 180, 200, 150],
        'Instagram (Users)': [180, 150, 200, 250, 150, 100, 100, 150, 100, 200, 150, 130, 200, 250, 150, 100, 100],
        'LinkedIn (Users)': [130, 100, 150, 180, 130, 250, 200, 180, 200, 180, 100, 200, 170, 150, 130, 250, 200],
        'YouTube (Users)': [250, 200, 250, 150, 100, 120, 170, 200, 150, 150, 250, 100, 130, 180, 100, 120, 170]}

# convert data to dataframe
df = pd.DataFrame(data)

# convert first column to string
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# plot the chart
fig, ax = plt.subplots(figsize=(10, 6))

# randomly set background grid lines
plt.grid(color='lightgrey', linestyle='--', linewidth=0.5)

# calculate max total value and set y limit and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/100.0)*100.0
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# set colors and transparency
colors = ['#0059B3', '#00A3E0', '#00CCFF', '#80DFFF', '#CCE6FF']
transparency = 0.7

# plot the chart
ax.stackplot(df['Category'], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], colors=colors, alpha=transparency)

# set legend
ax.legend(['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'YouTube'], loc='upper left', bbox_to_anchor=(1, 1))

# set x and y labels
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_xlabel('Category')
ax.set_ylabel('Number of Users')

# set title
plt.title('Social Media Usage by Industry')

# automatically resize the image
plt.tight_layout()

# save the chart
plt.savefig('output/final/area_chart/png/20231228-145339_50.png', dpi=100, bbox_inches='tight')

# clear the current image state
plt.clf()