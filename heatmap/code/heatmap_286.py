
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = {'Subject': ['Mathematics', 'English', 'Science', 'Social Studies', 'Art', 'Music'],
        'Elementary School': [80, 70, 85, 50, 90, 70],
        'Middle School': [75, 80, 85, 60, 85, 75],
        'High School': [70, 85, 90, 70, 80, 80]}

df = pd.DataFrame(data)
df = df.set_index('Subject')

fig, ax = plt.subplots(figsize=(10, 7))
sns.heatmap(df, annot=True, cmap='Blues', linewidths=.5, cbar=False, fmt='g')
ax.set_yticklabels(df.index, rotation=0, ha='right')
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_title('Performance in Different Subjects by Grade Level', fontsize=14)
ax.tick_params(axis='both', which='both', length=0, pad=8, labelsize=12)
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-163105_22.png', bbox_inches='tight')
plt.clf()