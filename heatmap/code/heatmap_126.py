


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Create a dictionary with the given data
data = {'Category': ['Fast Food', 'Casual Dining', 'Fine Dining', 'Cafes', 'Bars'],
        'Number of Restaurants': [500, 1000, 500, 750, 200],
        'Number of Fast Food Chains': [1000, 500, 150, 300, 100],
        'Number of Cafes': [250, 200, 50, 100, 50],
        'Number of Bars': [50, 400, 100, 50, 150],
        'Number of Bakeries': [100, 100, 75, 200, 75],
        'Number of Pizzerias': [300, 150, 50, 100, 50]}

# Convert the dictionary into a pandas dataframe
df = pd.DataFrame.from_dict(data)

# Set the index of the dataframe to the Category column
df.set_index('Category', inplace=True)

# Create a heatmap using seaborn
sns.set(font_scale=1.2) # Set the font scale for the heatmap
fig, ax = plt.subplots(figsize=(10,8)) # Set the figure size
sns.heatmap(df, annot=True, cmap='BuPu', fmt='g', ax=ax) # Create the heatmap with annotations and the BuPu color map
plt.title('Food and Beverage Industry by Category') # Set the title of the figure
plt.yticks(rotation=45, ha='right', rotation_mode='anchor') # Rotate the y-axis labels by 45 degrees
plt.tight_layout() # Automatically resize the image
plt.savefig('output/final/heatmap/png/20231228-131639_31.png', bbox_inches='tight') # Save the figure
plt.clf() # Clear the current image state