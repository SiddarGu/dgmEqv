

#import packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#get data
data = {'Product Category':['Electronics','Apparel','Home and Garden','Beauty Products','Toys and Games','Food and Beverage'],
        'Revenue ($)':['50B','35B','20B','15B','10B','5B'],
        'Profit Margin (%)':['10%','15%','12%','18%','8%','5%']}

#create dataframe
df = pd.DataFrame(data)

#convert data to numeric
df['Revenue ($)'] = df['Revenue ($)'].apply(lambda x: float(x.rstrip('B')))
df['Profit Margin (%)'] = df['Profit Margin (%)'].apply(lambda x: float(x.rstrip('%')))

#set figure size
plt.figure(figsize=(8,6))

#plot heatmap
sns.heatmap(df[['Revenue ($)','Profit Margin (%)']], annot=True, fmt='.0f', cmap='Blues', linewidths=0.5, cbar=True)

#set tick labels
plt.xticks(np.arange(2) + 0.5, ['Revenue ($)','Profit Margin (%)'], rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(6) + 0.5, ['Electronics','Apparel','Home and Garden','Beauty Products','Toys and Games','Food and Beverage'], rotation=0)

#set tick positions
plt.gca().set_xticks(np.arange(2) + 0.5, minor=True)
plt.gca().set_yticks(np.arange(6) + 0.5, minor=True)

#set tick labels in center
plt.gca().set_xticklabels(['Revenue ($)','Profit Margin (%)'], minor=True, ha='center')
plt.gca().set_yticklabels(['Electronics','Apparel','Home and Garden','Beauty Products','Toys and Games','Food and Beverage'], minor=True, va='center')

#add title
plt.title('Revenue and Profit by Product Category')

#resize image
plt.tight_layout()

#save image
plt.savefig('output/final/heatmap/png/20231228-162116_28.png', bbox_inches='tight')

#clear current image state
plt.clf()