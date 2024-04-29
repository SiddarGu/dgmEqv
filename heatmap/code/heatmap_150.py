
# Solution

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# data processing
data = {'Technology': ['Mobile', 'Internet of Things (IoT)', 'Cloud Computing', 'Artificial Intelligence (AI)', 'Augmented Reality (AR)', 'Virtual Reality (VR)'],
        'Total Revenue Generated (in millions)': [200000, 150000, 100000, 50000, 25000, 10000]}
df = pd.DataFrame(data)
df = df.set_index('Technology')

# plot the chart
fig, ax = plt.subplots(figsize=(10, 6))
heatmap = sns.heatmap(df, annot=True, cmap='YlGnBu', cbar_kws={'label': 'Revenue (in millions)'}, fmt='g')
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor', wrap=True)
heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation=0, ha='center')
ax.set_title('Revenue by Technology Sector')

# save the chart
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_7.png', bbox_inches='tight')

# clear the figure state
plt.clf()