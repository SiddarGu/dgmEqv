
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# import data
data = {'Category': ['Cloud Computing', 'Artificial Intelligence', 'Internet of Things', 'Virtual Reality', 'Blockchain', 'networking/n'],
        'Revenue ($B)': [200, 300, 150, 50, 100, 250],
        'Market Share (%)': [30, 25, 10, 5, 20, 10]}

# convert data to pandas dataframe
df = pd.DataFrame(data)

# set figure size
plt.figure(figsize=(8, 6))

# create heatmap with seaborn
ax = sns.heatmap(df.set_index('Category'), annot=True, cmap='Blues')

# set x and y ticks and tick labels
ax.set_yticks(np.arange(len(df['Category'])) + 0.5, minor=False)
# ax.set_xticks(np.arange(len(df['Market Share (%)'])) + 0.5, minor=False)
ax.set_yticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
# ax.set_xticklabels(df['Market Share (%)'], rotation=0, ha='center')

# set title
ax.set_title('Industry Dominance in Technology and the Internet')

# automatically resize image
plt.tight_layout()

# save figure
plt.savefig('output/final/heatmap/png/20231228-155147_1.png', bbox_inches='tight')

# clear current image state
plt.clf()