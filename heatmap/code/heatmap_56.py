
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define data in dictionary format
data = {'Sport': ['Basketball', 'Football', 'Soccer', 'Baseball', 'Hockey'],
        'Win Percentage (%)': [75, 80, 90, 70, 80],
        'Points': [25, 28, 2, 20, 10],
        'Assists': [11, 9, 0, 4, 12],
        'Rebounds': [8, 5, 1, 6, 5]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Reshape data to create a matrix for heatmap
# df_heatmap = df.pivot(index='Sport', columns='Player', values='Win Percentage (%)')

# Set figure size to prevent content from being displayed
fig = plt.figure(figsize=(10, 6))

# Create heatmap with seaborn.heatmap() and add a colorbar
# ax = sns.heatmap(df_heatmap, annot=True, cmap='Purples')
sns.heatmap(df.set_index('Sport'), annot=True, linewidths=.5, cmap='Purples', cbar=True)

# Set ticks and ticklabels for x and y axis, and make them in the center of rows and columns
plt.yticks(np.arange(len(df['Sport'])) + 0.5, df['Sport'], rotation=45, ha='right', rotation_mode='anchor')
plt.xticks(np.arange(4)+0.5, df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')

plt.title('Team and Player Performance in Major Sports')
# Automatically resize the image and save it
fig.tight_layout()

fig.savefig('output/final/heatmap/png/20231228-124154_43.png', bbox_inches='tight')

# Clear current image state

# Set title of the figure


# plt.clf()

# Create heatmap with imshow() and add a colorbar
# img = plt.imshow(df_heatmap, cmap='Purples')

# Add colorbar
# plt.colorbar(img)

# # Set ticks and ticklabels for x and y axis, and make them in the center of rows and columns
# plt.xticks(np.arange(len(df_heatmap.columns)), df_heatmap.columns, rotation=45, ha='right', rotation_mode='anchor')
# plt.yticks(np.arange(len(df_heatmap.index)), df_heatmap.index, rotation=0, ha='right', rotation_mode='anchor')

# # Show value of each cell
# for (j,i),label in np.ndenumerate(df_heatmap):
#     plt.text(i,j,label,ha='center',va='center')

# Automatically resize the image and save it
# plt.tight_layout()
# plt.savefig('output/final/heatmap/png/20231228-124154_43.png', bbox_inches='tight')

# Clear current image state
plt.clf()