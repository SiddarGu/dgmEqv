
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Convert data to dictionary
data = {'Year': [2017, 2018, 2019, 2020, 2021], 
        'Cases Filed': [500, 550, 600, 650, 700], 
        'Total Court Decisions': [400, 410, 420, 430, 440], 
        'Appeals Filed': [250, 260, 270, 280, 290], 
        'Appeals Won': [150, 160, 170, 180, 190]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Set axes
ax = plt.axes()

# Calculate max total value
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 100) * 100

# Set y-axis ticks and ticklabels
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x-axis ticks and ticklabels
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# Set background grid lines
ax.grid(True, alpha=0.5)

# Plot the data with area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=['Cases Filed', 'Total Court Decisions', 'Appeals Filed', 'Appeals Won'], colors=['#8B4C39', '#F2A900', '#00A6ED', '#009900'], alpha=0.8)

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Litigation Trends in the Legal System')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231226-103019_23.png', bbox_inches='tight')

# Clear current image state
plt.clf()