
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create dictionary from data
data = {'Subject': ['Science', 'Arts', 'History', 'Language', 'Social Science', 'Literature', 'Music', 'Physical Education'], 'Physics (%)': [30, 20, 25, 25, 20, 30, 25, 25], 'Chemistry (%)': [25, 30, 20, 25, 25, 20, 30, 25], 'Biology (%)': [25, 25, 30, 20, 25, 25, 20, 30], 'Mathematics (%)': [20, 25, 25, 30, 30, 25, 25, 20]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Set transparency and colors
colors = ['#3CB371', '#FF6347', '#4169E1', '#FF8C00']
alpha = 0.7

# Plot area chart
ax = plt.axes()
ax.stackplot(df.index, df.iloc[:, 1:].T, labels=df.columns[1:], colors=colors, alpha=alpha)

# Set x and y axis labels
ax.set_xlabel('Subjects')
ax.set_ylabel('Percentage of Students')

# Set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(df.index)
    ax.set_xticklabels(df.iloc[:, 0])
    ax.set_xlim(0, len(df.index) - 1)

    # Calculate max total value and set y axis ticks and ticklabels
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
    ax.set_yticks(yticks)
    ax.set_yticklabels([str(ytick) + '%' for ytick in yticks])

# Set background grid lines
ax.grid(ls='--', alpha=0.3)

# Set legend
handles, labels = ax.get_legend_handles_labels()
legend = ax.legend(handles[::-1], labels[::-1], bbox_to_anchor=(1, 1), loc='upper left', ncol=1, frameon=False)

# Set title
plt.title('Academic Subjects and their Percentage of Students')

# Automatically resize image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_86.png', bbox_inches='tight')

# Clear current image state
plt.clf()