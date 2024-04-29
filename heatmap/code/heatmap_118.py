
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define data
data = {'Category':['Sociology','Psychology','Anthropology','Economics','Political Science','History','Education'],
        'Books (Number)':[150,200,100,300,250,175,225],
        'Articles (Number)':[500,600,300,800,700,550,650],
        'Conferences (Number)':[10,12,8,15,14,11,13],
        'Journals (Number)':[25,30,20,35,32,28,31],
        'Citations (Number)':[2500,3000,1500,3500,3200,2750,3100],
        'Impact Factor':[3.5,3.8,3.2,4.2,4.0,3.6,3.9]
       }

# Convert data to dataframe
df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

# Set figure size
fig, ax = plt.subplots(figsize=(10,8))

# Plot heatmap using seaborn
sns.heatmap(df, cmap='coolwarm', annot=True, fmt='.1f', linewidths=0.5, ax=ax)

# Set x and y tick labels
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
# ax.set_yticklabels(df[['Books (Number)','Articles (Number)','Conferences (Number)','Journals (Number)','Citations (Number)','Impact Factor']].columns, rotation=0, ha='right', rotation_mode='anchor')

# Set ticks and ticklabels in the center of rows and columns
# ax.set_xticks(np.arange(0.5, 6.5, 1))
# ax.set_yticks(np.arange(0.5, 6.5, 1))

# Set title
ax.set_title('Research Output in Social Sciences and Humanities')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/heatmap/png/20231228-131639_22.png', bbox_inches='tight')

# Clear current image state
plt.clf()