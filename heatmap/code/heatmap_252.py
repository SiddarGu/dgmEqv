
# import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# create dictionary with data
data = {'Country': ['United States', 'China', 'Japan', 'Germany', 'United Kingdom'],
        'Tax Revenue (Billions)': [500, 400, 300, 200, 150],
        'Education Budget (Billions)': [200, 300, 200, 100, 100],
        'Infrastructure Spending (Billions)': [400, 500, 300, 200, 150],
        'Healthcare Budget (Billions)': [800, 600, 400, 300, 250],
        'Defense Budget (Billions)': [700, 600, 500, 400, 300]}

# convert dictionary to dataframe
df = pd.DataFrame(data)

# set country column as index
df.set_index('Country', inplace=True)

# create heatmap plot using seaborn
sns.heatmap(df, annot=True, cmap='viridis')

# set ticks and ticklabels for x and y axis
plt.xticks(np.arange(len(df.columns)) + 0.5, df.columns, rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(len(df.index)) + 0.5, df.index, rotation=0, ha='right', rotation_mode='anchor')

# set title
plt.title('Government Budget Allocation by Country')

# resize image
plt.tight_layout()

# save plot as png
plt.savefig('output/final/heatmap/png/20231228-155147_50.png', bbox_inches='tight')

# clear current image state
plt.clf()