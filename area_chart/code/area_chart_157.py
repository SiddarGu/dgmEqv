
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021], 
        'Facebook (Users)': [100, 120, 150, 180, 200, 220, 250], 
        'Instagram (Users)': [150, 180, 200, 220, 250, 270, 300], 
        'Twitter (Users)': [200, 220, 240, 260, 280, 300, 330], 
        'LinkedIn (Users)': [250, 260, 280, 300, 330, 350, 380], 
        'YouTube (Users)': [300, 320, 350, 380, 400, 420, 450]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 6))

# Create area chart using ax.stackplot()
ax = plt.axes()
ax.stackplot(df['Year'], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns)

# Set x and y axis labels and title
plt.xlabel('Year')
plt.ylabel('Number of Users')
plt.title('Social Media Platform Users by Year')

# Set ticks and ticklabels for x axis
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df['Year'])

# Calculate max total value and set y axis ticks and ticklabels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/10)*10
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
plt.grid(color='lightgrey', linestyle='dashed')

# Adjust legend position and add legend title
plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', title='Social Media Platform', framealpha=1)

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_77.png', bbox_inches='tight')

# Clear current image state
plt.clf()