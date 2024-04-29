
# Import python modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set data into dictionary
data = {'Category': ['Technology', 'Internet', 'Artificial Intelligence', 'Mobile Apps', 'E-commerce', 'Cybersecurity',
                     'Big Data', 'Virtual Reality', 'Gaming', 'Digital Marketing', 'Cloud Storage',
                     'Internet of Things', 'Web Development'],
        'Smartphones (Users)': [250, 300, 200, 180, 150, 100, 180, 100, 150, 180, 200, 250, 120],
        'Social Media (Users)': [300, 400, 250, 200, 180, 130, 200, 120, 180, 200, 220, 300, 150],
        'Online Shopping (Users)': [200, 250, 150, 300, 250, 150, 150, 150, 200, 220, 150, 200, 180],
        'Streaming Services (Users)': [150, 180, 120, 250, 300, 180, 120, 180, 220, 250, 120, 220, 200],
        'Cloud Computing (Users)': [220, 300, 180, 220, 200, 220, 180, 200, 250, 300, 180, 250, 220]}

# Process data with pandas
df = pd.DataFrame(data)
# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(20, 10))

# Set colors
colors = ['#FFCCCC', '#FF9999', '#FF6666', '#FF3333', '#FF0000']

# Set transparency
alpha = 0.8

# Set background grid lines
plt.grid(True, alpha=0.3)

# Set x and y axis ticks and ticklabels
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x and y axis limits
plt.xlim(0, len(df.index) - 1)
plt.ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10)

# Set x and y axis labels
plt.xlabel('Category')
plt.ylabel('Number of Users')

# Plot the chart
ax = plt.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5],
                   colors=colors, alpha=alpha)

# Set legend
plt.legend(ax, ['Smartphones', 'Social Media', 'Online Shopping', 'Streaming Services', 'Cloud Computing'],
           loc='upper left')

# Set title
plt.title('Technology and the Internet Usage Statistics')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-140159_1.png', bbox_inches='tight')

# Clear the current image state
plt.clf()