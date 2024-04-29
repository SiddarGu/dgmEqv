
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches

# Convert data to dictionary
data = {'Category': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania'], 'Corn (tons)': [10000, 9000, 8000, 7000, 6000, 5000], 'Wheat (tons)': [8000, 10000, 9000, 8000, 7000, 6000], 'Rice (tons)': [9000, 8000, 10000, 9000, 8000, 7000], 'Soybeans (tons)': [7000, 7000, 6000, 10000, 9000, 8000], 'Potatoes (tons)': [6000, 5000, 7000, 6000, 10000, 9000]}

# Convert dictionary to dataframe
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set colors for each category
colors = ['#FF7F50', '#FFD700', '#00BFFF', '#90EE90', '#FFC0CB', '#BA55D3']

# Plot the area chart
ax.stackplot(df['Category'], df['Corn (tons)'], df['Wheat (tons)'], df['Rice (tons)'], df['Soybeans (tons)'], df['Potatoes (tons)'], colors=colors, alpha=0.8)

# Set x and y axis ticks and ticklabels
# if np.random.random() >= 0.7:
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')


# max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# if max_total_value <= 10:
#     ax.set_yticks(np.linspace(0, 10, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
#     ax.set_ylim(0, 10)
# elif max_total_value <= 100:
#     ax.set_yticks(np.linspace(0, np.ceil(max_total_value), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
#     ax.set_ylim(0, np.ceil(max_total_value))
# elif max_total_value <= 1000:
#     ax.set_yticks(np.linspace(0, np.ceil(max_total_value), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
#     ax.set_ylim(0, np.ceil(max_total_value))
# else:
#     if max_total_value % 100 == 0:
#         ax.set_yticks(np.linspace(0, np.ceil(max_total_value), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
#         ax.set_ylim(0, np.ceil(max_total_value))
#     elif max_total_value % 100 == 10:
#         ax.set_yticks(np.linspace(0, np.ceil(max_total_value), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
#         ax.set_ylim(0, np.ceil(max_total_value))
#     else:
#         ax.set_yticks(np.linspace(0, np.ceil(max_total_value), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
#         ax.set_ylim(0, np.ceil(max_total_value))

# Set background grid lines
ax.grid(alpha=0.3)

# Set legend
corn_patch = mpatches.Patch(color=colors[0], label='Corn (tons)')
wheat_patch = mpatches.Patch(color=colors[1], label='Wheat (tons)')
rice_patch = mpatches.Patch(color=colors[2], label='Rice (tons)')
soybeans_patch = mpatches.Patch(color=colors[3], label='Soybeans (tons)')
potatoes_patch = mpatches.Patch(color=colors[4], label='Potatoes (tons)')
ax.legend(handles=[corn_patch, wheat_patch, rice_patch, soybeans_patch, potatoes_patch], loc='upper right')

# Set title
ax.set_title('Crop Production by Region')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-155112_34.png', bbox_inches='tight')

# Clear current image state
plt.clf()