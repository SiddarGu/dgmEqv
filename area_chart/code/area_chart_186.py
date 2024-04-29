
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create data dictionary
data = {
    'Category': ['Education', 'Healthcare', 'Social Services', 'Environment', 'Arts and Culture', 'Animal Welfare', 'Disaster Relief'],
    'Donations ($)': [20000, 30000, 25000, 15000, 10000, 20000, 30000],
    'Grants ($)': [50000, 40000, 35000, 30000, 20000, 25000, 50000],
    'Fundraising ($)': [15000, 20000, 10000, 25000, 5000, 15000, 30000],
}

# convert data to dataframe
df = pd.DataFrame(data)

# convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# set x and y axis ticks and labels
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# set colors and transparency
colors = ['#5F9EA0', '#7B68EE', '#FF7F50']
alpha = 0.5

# create stacked area chart
ax.stackplot(df['Category'], df['Donations ($)'], df['Grants ($)'], df['Fundraising ($)'], colors=colors, alpha=alpha)

# add background grid lines
ax.grid(axis='y', color='gray', linestyle='dashed', alpha=0.5)

# add legend
ax.legend(['Donations ($)', 'Grants ($)', 'Fundraising ($)'], loc='upper left', bbox_to_anchor=(1, 1))

# set title
ax.set_title('Charity and Nonprofit Organization Expenditures and Volunteer Involvement')

# automatically resize image
plt.tight_layout()

# save figure
plt.savefig('output/final/area_chart/png/20231228-145339_17.png', bbox_inches='tight')

# clear current image state
plt.clf()