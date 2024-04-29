

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#input data
data = {'Country': ['France', 'Spain', 'Italy', 'United Kingdom', 'Germany', 'United States'],
        'Hotel Occupancy (%)': [85, 80, 75, 70, 65, 60],
        'Average Room Rate (USD)': [120, 110, 100, 90, 80, 70],
        'Average Length of Stay (Days)': [7, 6, 5, 4, 3, 2],
        'Tourist Satisfaction (%)': [90, 85, 80, 75, 70, 65],
        'Number of Tourist Attractions': [350, 300, 280, 250, 230, 200]
       }

#convert data to pandas dataframe
df = pd.DataFrame(data)

#set figure size
plt.figure(figsize=(10,8))

#plot heatmap chart using seaborn
sns.heatmap(df.set_index('Country'), annot=True, fmt='g')

#set x and y axis ticks and labels
plt.xticks(np.arange(len(df.columns)), df.columns, rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(len(df)), df['Country'])

#set ticks and ticklabels in the center of rows and columns
plt.tick_params(axis='both', which='both', length=0, labelsize=12, pad=5)
ax = plt.gca()
ax.tick_params(axis='x', which='major', pad=10)
ax.tick_params(axis='y', which='major', pad=10)

#add title
plt.title('Key Metrics for Top Tourist Destinations', fontsize=16, pad=20)

#resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_44.png', bbox_inches='tight')

#clear current image state
plt.clf()