
# Importing necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Defining the data
data = {'Company': ['FedEx', 'UPS', 'DHL', 'USPS', 'Amazon Logistics'],
        'Shipment Volume (in billions)': [5.2, 4.8, 3.5, 2.5, 2.0],
        'Revenue (in billions)': [15.3, 14.2, 9.8, 7.2, 6.5],
        'Market Share (%)': [15, 14, 10, 7, 6],
        'Average Speed (mph)': [70, 65, 60, 55, 50],
        'On-time Arrival Rate (%)': [95, 93, 92, 90, 88]}

# Creating a dataframe from the data
df = pd.DataFrame(data)

# Setting the index as the Company names
df.set_index('Company', inplace=True)

# Creating a figure and axes object
fig, ax = plt.subplots(figsize=(10,8))

# Plotting the heatmap using sns.heatmap()
sns.heatmap(df, annot=True, fmt='g', cmap='YlGnBu', cbar=False)

# Setting the x and y ticks and ticklabels to be in the center of the cells
ax.set_xticks(np.arange(0.5, len(df.columns), 1))
ax.set_yticks(np.arange(0.5, len(df.index), 1))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Setting the title of the figure
ax.set_title('Shipping and Logistics Performance')

# Automatically resizing the figure and saving it
fig.tight_layout()
fig.savefig('output/final/heatmap/png/20231228-155147_30.png', bbox_inches='tight')

# Clearing the current image state
plt.clf()