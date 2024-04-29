


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data as a dictionary
data = {'Subject': ['Grade 9', 'Grade 10', 'Grade 11', 'Grade 12'],
        'Science (Hours)': [4, 5, 4, 6],
        'Mathematics (Hours)': [3, 3, 4, 4],
        'English (Hours)': [2, 3, 2, 3],
        'History (Hours)': [2, 2, 3, 2],
        'Physical Education (Hours)': [1, 1, 1, 1]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 6))

# Use ax instead of plt to plot the chart
ax = plt.gca()
ax.stackplot(df['Subject'], df['Science (Hours)'], df['Mathematics (Hours)'], df['English (Hours)'], df['History (Hours)'], df['Physical Education (Hours)'], labels=['Science', 'Mathematics', 'English', 'History', 'Physical Education'], colors=['#FFA07A', '#87CEEB', '#FFDAB9', '#F5DEB3', '#90EE90'], alpha=0.8)

# Add background grid lines
ax.grid(linestyle='dashed', color='grey')

# Set title
ax.set_title('Study Hours by Subject and Grade')

# Set x and y axis ticks and ticklabels
if np.random.rand() < 0.7:
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Subject'])
    ax.set_xlim(0, len(df.index) - 1)
    ax.tick_params(axis='x', labelrotation=45, ha='right', rotation_mode='anchor')
if np.random.rand() < 0.7:
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value < 10:
        yticks_len = 3
    elif max_total_value < 100:
        yticks_len = 5
    elif max_total_value < 1000:
        yticks_len = 7
    else:
        yticks_len = 9
    ax.set_yticks(np.linspace(0, max_total_value, yticks_len, dtype=np.int32))
    ax.set_ylim(0, np.ceil(max_total_value / 10) * 10)

# Set legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[::-1], labels=labels[::-1], loc='upper left')

# Automatically resize image
plt.tight_layout()

# Save the chart
plt.savefig('output/final/area_chart/png/20231228-145339_42.png', bbox_inches='tight')

# Clear the current image state
plt.clf()