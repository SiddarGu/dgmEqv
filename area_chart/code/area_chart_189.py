
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the data as a dictionary
data = {'Category':['Italian', 'Mexican', 'Chinese', 'American', 'Indian', 'Japanese', 'Thai', 'French', 'Mediterranean', 'Korean', 'Greek', 'Vietnamese', 'Brazilian'], 'Food ($)':[3000, 2500, 2800, 4000, 3500, 3000, 2500, 3500, 4000, 3000, 2500, 3500, 3000], 'Beverage ($)':[4000, 3500, 3000, 5000, 4500, 3500, 3000, 4000, 4500, 3500, 3000, 4000, 3500]}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
plt.figure(figsize=(10, 6))

# Plot the data as an area chart
ax = plt.gca()
ax.stackplot(df.index, df.iloc[:, 1], df.iloc[:, 2], labels=['Food ($)', 'Beverage ($)'], colors=['#ffcc99', '#99ccff'], alpha=0.7)

# Set the x and y-axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(df.index)
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', wrap=True, rotation_mode='anchor')
    
    # Calculate the max total value
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    
    # Ceil max_total_value up to the nearest multiple of 10, 100 or 1000
    if max_total_value < 100:
        max_total_value = np.ceil(max_total_value/10)*10
    elif max_total_value < 1000:
        max_total_value = np.ceil(max_total_value/100)*100
    else:
        max_total_value = np.ceil(max_total_value/1000)*1000
    
    # Set the y-axis ticks and ticklabels
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    
# Set background grid lines
ax.grid(color='#cccccc', linestyle='dotted')

# Set the legend
ax.legend(loc='upper left')

# Set the title
ax.set_title('Food and Beverage Sales by Cuisine Type')

# Automatically resize the image
plt.tight_layout()

# Save the image as a png file
plt.savefig('output/final/area_chart/png/20231228-145339_20.png', bbox_inches='tight')

# Clear the current image state
plt.clf()