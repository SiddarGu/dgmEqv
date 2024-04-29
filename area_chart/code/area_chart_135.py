
# 1. Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 2. Define the data as a dictionary and convert the first column to string type
data = {'Policy Area': ['Agriculture', 'Environment', 'Education', 'Healthcare', 'Public Safety', 'Economic Development'], 'Energy (%)': [20, 15, 10, 25, 15, 15], 'Education (%)': [10, 20, 30, 20, 15, 5], 'Healthcare (%)': [30, 25, 20, 30, 15, 10], 'Infrastructure (%)': [20, 25, 10, 15, 20, 20], 'Social Services (%)': [20, 15, 30, 10, 35, 50]}
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# 3. Set the figure size and create a new figure
fig, ax = plt.subplots(figsize=(12, 8))

# 4. Plot the data using the stackplot() function
ax.stackplot(df.index, df['Energy (%)'], df['Education (%)'], df['Healthcare (%)'], df['Infrastructure (%)'], df['Social Services (%)'], labels=['Energy', 'Education', 'Healthcare', 'Infrastructure', 'Social Services'])

# 5. Set the x and y axis ticks and ticklabels
if np.random.rand() < 0.7:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(df.index)
    ax.set_xticklabels(df['Policy Area'], rotation=45, ha='right', rotation_mode='anchor')
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# 6. Set colors and transparency for the plot
colors = ['#4472C4', '#ED7D31', '#A5A5A5', '#FFC000', '#5B9BD5']
ax.set_prop_cycle(color=colors)
alpha = 0.8

# 7. Add grid lines
ax.grid(True, color='#ECECEC', linestyle='-', linewidth=0.5)

# 8. Adjust the legend's position
ax.legend(loc='upper left', frameon=False)

# 9. Automatically resize the image
fig.tight_layout()

# 10. Set the figure title and save the image
ax.set_title('Government Policy Priorities by Sector')
fig.savefig('output/final/area_chart/png/20231228-140159_49.png', bbox_inches='tight')

# 11. Clear the current image state
plt.clf()
plt.close()