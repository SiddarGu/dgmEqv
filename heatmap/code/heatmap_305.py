

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Process data
field_list = ['Physics', 'Chemistry', 'Biology', 'Computer Science', 'Mathematics', 'Engineering']
major_list = ['Aerospace', 'Biomedical', 'Civil', 'Mechanical', 'Electrical']
data_list = [[25, 15, 12, 18, 10, 20],
             [15, 12, 20, 8, 25, 20],
             [20, 25, 15, 8, 10, 22],
             [18, 20, 25, 15, 12, 10],
             [22, 18, 25, 20, 15, 12]]

# Create dataframe
df = pd.DataFrame(data_list, columns=field_list, index=major_list)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Plot heatmap
heatmap = sns.heatmap(df, annot=True, cmap='Blues', ax=ax, cbar=False)

# Set x and y ticks and labels
ax.set_xticklabels(field_list, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(major_list, rotation=0)

# Set title
ax.set_title('Field-wise Distribution of Science and Engineering Majors')

# Automatically resize image
fig.tight_layout()

# Save figure
plt.savefig('output/final/heatmap/png/20231228-163105_9.png', bbox_inches='tight')
# Clear current image state
plt.clf()