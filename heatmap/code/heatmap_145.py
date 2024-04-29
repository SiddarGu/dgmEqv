
# import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create a dictionary with the given data
data_dict = {'Category': ['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Toys'],
            'Online Sales ($)': [500000, 1000000, 750000, 250000, 375000],
            'In-Store Sales ($)': [250000, 500000, 375000, 125000, 187500],
            'Total Sales ($)': [750000, 1500000, 1125000, 375000, 562500],
            'Online Share (%)': [67.5, 66.7, 66.7, 66.7, 66.7],
            'In-Store Share (%)': [32.5, 33.3, 33.3, 33.3, 33.3]
            }

# convert the dictionary to a pandas dataframe
df = pd.DataFrame(data_dict)

# get the labels for x and y axis
x_labels = ['Online Sales ($)', 'In-Store Sales ($)', 'Total Sales ($)']
y_labels = ['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Toys']

# create a figure and axis object using subplots()
fig, ax = plt.subplots(figsize=(8, 6))

# plot the heatmap chart using seaborn
import seaborn as sns
sns.heatmap(df.set_index('Category')[x_labels], annot=True, fmt='.0f', cmap='Blues', cbar=False, ax=ax)

# set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(0, len(x_labels)) + 0.5)
ax.set_xticklabels(x_labels, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(0, len(y_labels)) + 0.5)
ax.set_yticklabels(y_labels, rotation=0, ha='right', rotation_mode='anchor')

# set the title of the figure
plt.title('Retail and E-commerce Sales by Category')

# automatically resize the image by tight_layout()
plt.tight_layout()

# save the figure
plt.savefig('output/final/heatmap/png/20231228-131639_63.png', bbox_inches='tight')

# clear the current image state
plt.clf()