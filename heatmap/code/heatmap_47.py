

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = {
    'Technology': [50, 45, 40, 35, 30, 25],
    'Internet': [25, 27, 30, 33, 36, 40],
    'Cloud Computing': [10, 12, 15, 17, 20, 22],
    'AI': [5, 7, 8, 10, 12, 13],
    'Blockchain': [5, 5, 4, 3, 2, 0],
    'Virtual Reality': [5, 4, 3, 2, 0, 0],
    'Internet of Things': [5, 4, 3, 2, 0, 0]
}

df = pd.DataFrame(data, index=[2015, 2016, 2017, 2018, 2019, 2020])

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(df, annot=False, cmap='YlOrBr', linewidths=0.5, cbar_kws={'label': 'Percentage'}, ax=ax)
ax.tick_params(axis='both', which='both', length=0, labelsize=14)
ax.set_title('Evolution of Technology and the Internet', fontsize=16)
ax.set_xlabel('Technology', fontsize=14)
ax.set_ylabel('Year', fontsize=14)
ax.set_yticklabels(ax.get_yticklabels(), rotation=45, ha='right', rotation_mode='anchor')

plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_35.png', bbox_inches='tight')
plt.show()

# Clear the current image state
plt.clf()