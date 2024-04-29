
#import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#set data
data = {'Category': ['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Toys'],
        'Number of Stores': [500, 700, 300, 400, 200],
        'Total Revenue (Millions)': [3500, 4500, 2000, 3000, 1500],
        'Average Revenue per Store (Millions)': [7, 6.4, 6.7, 7.5, 7.5],
        'Number of Employees': [1000, 1200, 800, 900, 600],
        'Total Expenses (Millions)': [2800, 3200, 1800, 2400, 1200],
        'Average Expenses per Store (Millions)': [5.6, 4.6, 6, 6, 6]}

#create dataframe
df = pd.DataFrame(data)

#set figure size
plt.figure(figsize=(12,8))

#plot heatmap chart using seaborn
ax = sns.heatmap(df[['Number of Stores', 'Total Revenue (Millions)', 'Average Revenue per Store (Millions)', 'Number of Employees', 'Total Expenses (Millions)', 'Average Expenses per Store (Millions)']], cmap='Blues', annot=True, fmt='.1f', linewidths=.5, annot_kws={'size': 12}, cbar=True, cbar_kws={'shrink': .5})

#set ticks and ticklabels for x-axis
ax.set_xticks(np.arange(len(df.columns[1:])) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.xaxis.set_ticks_position('top')

#set ticks and ticklabels for y-axis
ax.set_yticks(np.arange(len(df['Category'])) + 0.5)
ax.set_yticklabels(df['Category'], rotation=0, wrap=True, va='center', ha='right')
ax.yaxis.set_ticks_position('left')

#set title
plt.title('Retail Metrics by Category')

#automatically resize the image
plt.tight_layout()

#save image
plt.savefig('output/final/heatmap/png/20231228-163105_1.png', bbox_inches='tight')

#clear current image state
plt.clf()

#check the code
print('The code is generated successfully.')