
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data processing
data = {'Subject': ['Mathematics', 'Sciences', 'Language Arts', 'History', 'Foreign Language', 'Arts', 'Physical Education'],
        'Student.1': [85, 90, 92, 80, 88, 70, 95],
        'Student.2': [90, 85, 88, 85, 90, 72, 90],
        'Student.3': [88, 92, 90, 85, 85, 75, 92],
        'Student.4': [80, 85, 82, 90, 92, 80, 85],
        'Student.5': [92, 88, 85, 82, 80, 90, 88],
        'Student.6': [85, 90, 92, 80, 88, 70, 85]}

df = pd.DataFrame(data)
df.set_index('Subject', inplace=True)

# Plotting chart
fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(df, cmap='Blues', interpolation='none')

# Add ticks and tick labels
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index)

# Center ticks
ax.tick_params(axis='both', which='both', length=0)
ax.tick_params(axis='x', which='major', pad=15)

# Add text annotations
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        ax.text(j, i, df.iloc[i, j], ha='center', va='center', color='black')

# Add colorbar
cbar = fig.colorbar(im)

# Set title
ax.set_title('Student Performance Across Subjects', fontweight='bold')

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-155147_5.png', bbox_inches='tight')

# Clear image state
plt.clf()