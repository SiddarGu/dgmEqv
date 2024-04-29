
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define the data
data = {'Law Firm': ['Davis & Co.', 'Smith & Jones', 'Johnson & Smith'],
        'Number of Partners': [20, 30, 25],
        'Number of Associates': [50, 75, 60],
        'Number of Legal Assistants': [100, 150, 110],
        'Revenue ($)': [5000000, 7500000, 6000000],
        'Number of Clients': [200, 250, 225]}

# Convert the data into a dataframe
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(10, 8))

# Plot the heatmap using sns.heatmap()
sns.heatmap(df.set_index('Law Firm'), annot=True, cmap='Blues')

# Set the ticks and tick labels for x and y axis
plt.xticks(np.arange(5), ('Number of Partners', 'Number of Associates', 'Number of Legal Assistants', 'Revenue ($)', 'Number of Clients'), rotation=45, ha='right', rotation_mode='anchor')
plt.yticks(np.arange(3), ('Davis & Co.', 'Smith & Jones', 'Johnson & Smith'), rotation=0)

# Set the title of the figure
plt.title('Law Firm Performance Metrics')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/heatmap/png/20231228-131639_95.png', bbox_inches='tight')

# Clear the current image state
plt.clf()