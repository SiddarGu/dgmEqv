
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# define data dictionary
data_dict = {
    'Category': ['Social Media Usage', 'Mobile Internet Usage', 'Online Shopping', 'E-commerce Sales', 'Cybersecurity Spending'],
    '2018 (%)': [30, 25, 20, 15, 10],
    '2019 (%)': [35, 30, 25, 20, 15],
    '2020 (%)': [40, 35, 30, 25, 20],
    '2021 (%)': [45, 40, 35, 30, 25],
    '2022 (%)': [50, 45, 40, 35, 30]
}

# convert data dictionary to dataframe
df = pd.DataFrame(data_dict)

# set index to Category
df.set_index('Category', inplace=True)

# create heatmap using seaborn
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df, annot=True, cmap='Blues', fmt='g', center=True)

# set ticks and tick labels
ax.set_xticks(np.arange(len(df.columns))+0.5)
ax.set_yticks(np.arange(len(df))+0.5)
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor', wrap=True)

# set title
ax.set_title('Technology and Internet Trends')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_75.png', bbox_inches='tight')

# clear image state
plt.clf()