


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# define data using a dictionary and convert first column to string type
data = {'Category': ['Communication', 'Entertainment', 'E-commerce', 'Education', 'Finance', 'Healthcare', 'Business', 'Gaming', 'Travel', 'Social Networking', 'News', 'Navigation', 'Sports'], 
        'Mobile Users': [200, 400, 300, 200, 150, 300, 200, 100, 50, 400, 150, 100, 200], 
        'Online Shoppers': [300, 250, 400, 150, 200, 150, 250, 200, 100, 350, 100, 200, 300], 
        'Internet Speed': [50, 60, 120, 80, 40, 70, 90, 30, 40, 100, 50, 80, 60], 
        'Smartphone Penetration': [80, 90, 70, 60, 100, 50, 80, 60, 70, 90, 80, 60, 50]}

df = pd.DataFrame(data) # process data using pandas
df.iloc[:, 0] = df.iloc[:, 0].astype(str) # convert first column to string type

# plot data using area chart
fig, ax = plt.subplots(figsize=(10, 6)) # set larger figsize to prevent content from being displayed
ax.stackplot(df.index, df.iloc[:, 1:].T, labels=df.columns[1:], colors=['#FFC300', '#900C3F', '#FF5733', '#C70039', '#6C3483', '#16A085', '#1D8348', '#F4D03F', '#3498DB', '#8E44AD', '#F1C40F', '#2ECC71', '#5D6D7E'], alpha=0.7) # plot stackplot with suitable colors and transparency

# randomly set background grid lines
ax.grid(color='black', linestyle='dotted', linewidth=0.5)

# set ticks and ticklabels for x and y axis with a 70% probability
# if np.random.choice([True, False], p=[0.7, 0.3]):
ax.set_xlim(0, len(df.index) - 1) # set x axis ticks
ax.set_xticks(df.index) # set x axis ticklabels
ax.set_xticklabels(df['Category'], rotation=45, ha='right', wrap=True) # use rotation and wrap to prevent 
# ax.set_yticklabels(df.columns[1:])
# label overlapping
# if np.random.choice([True, False], p=[0.7, 0.3]):
#     max_total_value = df.iloc[:, 1:].sum(axis=1).max() # calculate max total value
#     max_total_value = np.ceil(max_total_value / 10) * 10 # ceil max total value up to nearest multiple of 10
#     ax.set_ylim(0, max_total_value) # set y axis range
#     ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) # set y axis ticks
#     ax.set_yticklabels(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) # set y axis ticklabels
#     ax.set_ylabel('Count') # set y axis label

# set legend and title
ax.legend(loc='upper left') # adjust legend position to avoid overlapping
ax.set_title('Technology and the Internet Trends and Usage') # set title

# automatically resize image and save
fig.tight_layout() # use tight_layout() to resize image
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/area_chart/png_train/area_chart_265.png', bbox_inches='tight') # save image with relative path and bbox_inches='tight' parameter

# clear current image state
plt.clf()