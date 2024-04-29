

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Process data
data = {
    'Discipline': ['Psychology', 'Sociology', 'History', 'Economics', 'Political Science'],
    '2018 (%)': [20, 18, 15, 22, 16],
    '2019 (%)': [22, 20, 18, 24, 18],
    '2020 (%)': [24, 22, 20, 26, 19],
    '2021 (%)': [25, 23, 21, 27, 20],
    '2022 (%)': [26, 24, 22, 28, 21]
}

df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 8))

# Plot heatmap using seaborn
sns.heatmap(df.set_index('Discipline'), annot=True, cmap='coolwarm', fmt='g', annot_kws={'size': 12})

# Set ticks and tick labels
# plt.xticks(np.arange(len(df.columns)) + 0.5, labels=df.columns, rotation=45, ha='right', rotation_mode='anchor')
# plt.yticks(np.arange(len(df.index)) + 0.5, labels=df.index, rotation=0)

# Set title
plt.title('Growth in Social Sciences and Humanities Disciplines')

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-134212_63.png', bbox_inches='tight')

# Clear current image state
plt.clf()