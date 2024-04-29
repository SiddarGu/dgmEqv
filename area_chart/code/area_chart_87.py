
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define data as a dictionary
data = {'Category': ['Chemistry', 'Physics', 'Biology', 'Mathematics', 'Engineering'],
        '2010': [500, 600, 550, 700, 800],
        '2011': [520, 650, 580, 720, 820],
        '2012': [530, 670, 600, 730, 840],
        '2013': [550, 680, 620, 740, 860],
        '2014': [560, 690, 630, 750, 870],
        '2015': [570, 700, 640, 760, 880],
        '2016': [580, 710, 650, 770, 890],
        '2017': [590, 720, 660, 780, 900],
        '2018': [600, 730, 670, 790, 910],
        '2019': [610, 740, 680, 800, 920],
        '2020': [620, 750, 690, 810, 930]
        }

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 6))

# Plot the data with area chart
ax = plt.axes()
ax.stackplot(df['Category'], df.iloc[:, 1:].values.T, labels=df.columns[1:], alpha=0.7)

# Set x and y axis labels
ax.set_xlabel('Category')
ax.set_ylabel('Publications')

# Set title
plt.title('Publications in Science and Engineering by Category from 2010 to 2020')

# Set background grid lines
ax.grid(linestyle='--', alpha=0.5)

# Set legend and adjust position
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('output/final/area_chart/png/20231228-131755_70.png', bbox_inches='tight')

# Clear the current image state
plt.clf()