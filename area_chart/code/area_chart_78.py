
# Solution

# import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# define the data
data = {'Category': ['Advertising', 'Influencers', 'E-commerce', 'Brand Awareness', 'Customer Engagement', 'Content Creation', 'Analytics', 'Customer Service', 'News and Updates', 'Event Promotion', 'Social Listening', 'Community Management', 'Social Media Strategy'], 
        'Facebook (Users)': [200, 100, 150, 100, 200, 150, 180, 130, 250, 120, 180, 150, 120], 
        'Instagram (Users)': [180, 120, 180, 200, 180, 200, 150, 100, 130, 100, 200, 180, 150], 
        'Twitter (Users)': [150, 150, 200, 250, 150, 100, 100, 150, 100, 200, 150, 130, 200], 
        'LinkedIn (Users)': [130, 100, 150, 180, 130, 250, 200, 180, 200, 180, 100, 200, 170], 
        'YouTube (Users)': [100, 200, 250, 150, 100, 120, 170, 200, 150, 150, 250, 100, 130]}

# convert data to pandas dataframe
df = pd.DataFrame(data)

# convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figure size
fig, ax = plt.subplots(figsize=(10,6))

# stackplot the data
ax.stackplot(df.index, 
             df.iloc[:, 1], 
             df.iloc[:, 2], 
             df.iloc[:, 3], 
             df.iloc[:, 4], 
             df.iloc[:, 5], 
             labels=['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'YouTube'], 
             colors=['#3b5998', '#e4405f', '#1da1f2', '#0077b5', '#c4302b'], 
             alpha=0.8)

# randomly set background grid lines
ax.grid(color='#CCCCCC', linestyle=':', linewidth=0.5)

# set x and y axis labels
ax.set_xlabel('Categories')
ax.set_ylabel('Number of Users')

# set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(df.index)
    ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
else:
    ax.set_xticks([])
    ax.set_yticks([])

# set suitable y axis range
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value <= 10:
    ax.set_ylim(0, 10)
elif max_total_value <= 100:
    ax.set_ylim(0, np.ceil(max_total_value/10)*10)
elif max_total_value <= 1000:
    ax.set_ylim(0, np.ceil(max_total_value/100)*100)

# set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# set title
ax.set_title('Social Media Usage by Industry Categories')

# automatically resize the image
fig.tight_layout()

# save the image
fig.savefig('output/final/area_chart/png/20231228-131755_60.png', bbox_inches='tight')

# clear the current image state
plt.clf()