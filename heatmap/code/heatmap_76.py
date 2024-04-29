
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {"Year": ["2020", "2021", "2022", "2023", "2024"], "Beverage Sales (in millions)": [500, 550, 600, 650, 700], "Food Sales (in millions)": [800, 850, 900, 950, 1000]}

df = pd.DataFrame(data)
df.set_index("Year", inplace=True)

# set the figure size to a larger setting
fig = plt.figure(figsize=(8, 6))

# plot the heatmap chart using ax
ax = plt.axes()

# use imshow() or pcolor() with 70% probability
if np.random.rand() < 0.7:
    im = ax.imshow(df, cmap='coolwarm')
# use sns.heatmap() with 30% probability
else:
    import seaborn as sns
    im = sns.heatmap(df, cmap='coolwarm')

# add colorbar with 40% probability
if np.random.rand() < 0.4:
    plt.colorbar(im)

# add ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(len(df.index)))
ax.set_yticklabels(df.index)

# make ticks and ticklabels in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns)) + 0.5, minor=True)
ax.set_yticks(np.arange(len(df.index)) + 0.5, minor=True)
ax.tick_params(which='minor', length=0)

# show the value of each cell if no colorbar is added
if not plt.colorbar(im):
    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            text = ax.text(j, i, df.iloc[i, j], ha='center', va='center', color='w')

# set title
plt.title('Forecasted Sales in Food and Beverage Industry')

# resize the image
plt.tight_layout()

# save the chart as output/final/heatmap/png/20231228-124154_68.png
plt.savefig('output/final/heatmap/png/20231228-124154_68.png', bbox_inches='tight')

# clear the current image state
plt.clf()