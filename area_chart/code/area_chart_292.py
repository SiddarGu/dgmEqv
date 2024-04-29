
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import MultipleLocator

# Create a dictionary of data
data = {'Field': ['Biology', 'Chemistry', 'Physics', 'Engineering', 'Computer Science', 'Mathematics', 'Environmental Science', 'Astronomy', 'Geology', 'Robotics'],
        'Research Projects': [100, 120, 150, 200, 250, 200, 180, 150, 130, 100],
        'Publications': [150, 100, 130, 180, 200, 150, 200, 220, 180, 250],
        'Patents': [50, 80, 70, 100, 120, 90, 100, 110, 120, 130],
        'Awards': [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],
        'Conferences': [10, 15, 25, 30, 35, 40, 45, 50, 55, 60]}

# Convert the data into a dataframe
df = pd.DataFrame(data)

# Convert the first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
fig, ax = plt.subplots(figsize = (12, 8))

# Set the x and y axis ticks and tick labels
ax.set_xlim(0, len(df.index) - 1)
ax.yaxis.set_major_locator(MaxNLocator(nbins = 5))
ax.set_xticks(np.arange(len(df)))
ax.set_xticklabels(df['Field'])
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis = 1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype = np.int32))

# Set the background grid lines
ax.grid(color = 'lightgrey', linestyle = '--', linewidth = 0.5, alpha = 0.5)

# Calculate the max total value and set the y limit range
max_total_value = df.iloc[:, 1:].sum(axis = 1).max()
ax.set_ylim(0, np.ceil(max_total_value / 10) * 10)

# Plot the data as an area chart
ax.stackplot(df.index, df['Research Projects'], df['Publications'], df['Patents'], df['Awards'], df['Conferences'], labels = ['Research Projects', 'Publications', 'Patents', 'Awards', 'Conferences'], colors = ['lightblue', 'green', 'orange', 'red', 'purple'], alpha = 0.7)
plt.xticks(rotation=90, ha='right', rotation_mode='anchor')

# Set the legend and its position
ax.legend(loc = 'upper left', bbox_to_anchor = (1.02, 1), borderaxespad = 0)

# Set the title and labels
ax.set_title('Science and Engineering Accomplishments by Field')
ax.set_xlabel('Field')
ax.set_ylabel('Number of Accomplishments')

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-155112_8.png', bbox_inches = 'tight')

# Clear the current image state
plt.clf() 