
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#data processing
data = {'Organization': ['Red Cross', 'Salvation Army', 'Doctors Without Borders', 'Habitat for Humanity', 'World Wildlife Fund'], 
        'Donations (in thousands)': [500, 300, 200, 150, 100], 
        'Fundraising Expenses (in thousands)': [100, 75, 50, 40, 30], 
        'Program Expenses (in thousands)': [350, 225, 150, 110, 70], 
        'Administrative Expenses (in thousands)': [50, 50, 50, 20, 20], 
        'Net Assets (in thousands)': [50000, 40000, 30000, 20000, 15000]}

df = pd.DataFrame(data, columns = ['Organization', 'Donations (in thousands)', 'Fundraising Expenses (in thousands)', 'Program Expenses (in thousands)', 'Administrative Expenses (in thousands)', 'Net Assets (in thousands)'])

#plotting the heatmap
fig, ax = plt.subplots(figsize=(12,8))

#using seaborn heatmap
#sns.heatmap(df.iloc[:, 1:], annot=True, cbar=False, cmap="Blues", fmt='g')

#using pcolor
sns.set(font_scale=1.2)
im = ax.pcolor(df.iloc[:, 1:], cmap="Blues", edgecolors='white', linewidths=2)

#customize tick labels
ax.set_xticks(np.arange(0.5, len(df.columns)-1, 1))
ax.set_yticks(np.arange(0.5, len(df), 1))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df['Organization'], wrap=True)

#center the ticks
ax.set_xticks(np.arange(len(df.columns)-1)+0.5, minor=False)
ax.set_yticks(np.arange(len(df))+0.5, minor=False)

#add colorbar
cbar = plt.colorbar(im, ax=ax)

#set title
plt.title("Financial Overview of Top Nonprofits")

#resize and save figure
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-130949_3.png', bbox_inches='tight')

#clear image state
plt.clf()