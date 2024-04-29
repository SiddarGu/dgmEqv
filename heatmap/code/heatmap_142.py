
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# data
data = {'Category': ['Sociology', 'Psychology', 'History', 'Anthropology', 'Political Science', 'Economics', 'Geography', 'Linguistics', 'Philosophy'],
        'Research Productivity (Publications per Year)': [4.5, 6.2, 3.8, 5.5, 3.2, 4.0, 2.8, 4.2, 3.5],
        'Citations per Publication': [15, 20, 18, 22, 16, 17, 14, 19, 18],
        'Research Funding (Million USD)': [10, 12, 8, 13, 9, 11, 7, 10, 8],
        'Graduate Students': [50, 75, 40, 60, 45, 55, 35, 50, 40],
        'Undergraduate Students': [200, 150, 100, 120, 75, 80, 50, 100, 80],
        'Research Staff': [75, 60, 50, 55, 45, 40, 30, 45, 35]
        }

# convert data to dataframe
df = pd.DataFrame(data)

# set category as index
df.set_index('Category', inplace=True)

# create figure and axes
fig, ax = plt.subplots(figsize=(12,6))

# plot heatmap
heatmap = ax.imshow(df, cmap='Blues')

# add colorbar
if np.random.randint(0, 10) < 4:
    cbar = plt.colorbar(heatmap)

# show values in each cell
if np.random.randint(0, 10) < 4:
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            text = ax.text(j, i, df.iloc[i, j],
                           ha="center", va="center", color="w")

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(df.shape[1]))
ax.set_yticks(np.arange(df.shape[0]))
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# rotate x and y ticklabels if length is more than 6 characters
if max([len(x) for x in df.columns]) > 6:
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
if max([len(x) for x in df.index]) > 6:
    plt.setp(ax.get_yticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# set ticks and ticklabels in the center of rows and columns
ax.tick_params(direction='inout')
ax.tick_params(axis='both', which='major', pad=10)

# add title and axis labels
plt.title('Research Productivity and Funding in Social Sciences and Humanities')
plt.xlabel('Research Metrics')
plt.ylabel('Disciplines')

# resize image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-131639_58.png', bbox_inches='tight')