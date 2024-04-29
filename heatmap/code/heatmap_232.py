
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Process the data using dict and pandas
data = {'Team':['New York Yankees', 'Los Angeles Lakers', 'Real Madrid', 'New England Patriots'],
        'Wins':[108, 52, 28, 11],
        'Losses':[54, 20, 8, 5],
        'Draws':[0, 0, 2, 0],
        'Points For':[943, 110.2, 102, 436],
        'Points Against':[739, 105.5, 42, 325],
        'Win Percentage':[66.67, 72.22, 77.78, 68.75]}

df = pd.DataFrame(data)
df.set_index('Team', inplace=True)

# Plot the data using heatmap chart
fig, ax = plt.subplots(figsize=(10, 8))
heatmap = ax.imshow(df, cmap='coolwarm')

# Set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# Make the ticks and ticklabels in the center of rows and columns
# ax.set_xticks(np.arange(len(df.columns)+1), minor=True)
# ax.set_yticks(np.arange(len(df.index)+1), minor=True)
# ax.tick_params(which='minor', bottom=False, left=False)

# Rotate the x-axis ticklabels by 45 and set the rotation mode and anchor
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Add the colorbar and set the title
cbar = fig.colorbar(heatmap)
cbar.set_label('Value')
ax.set_title('Team Performance Metrics')

# Automatically resize the image and save it
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_21.png', bbox_inches='tight')

# Clear the current image state
plt.clf()