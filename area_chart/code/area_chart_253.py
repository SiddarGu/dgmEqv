
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define the data as a dictionary
data = {'Category': ['Food', 'Clothing', 'Electronics', 'Beauty', 'Home Goods', 'Sporting Goods', 'Furniture', 'Toys', 'Books', 'Jewelry', 'Automotive', 'Appliances', 'Health & Wellness'],
        'Retail Sales ($)': [500000, 400000, 600000, 300000, 700000, 200000, 800000, 100000, 150000, 900000, 600000, 400000, 200000],
        'E-commerce Sales ($)': [1000000, 800000, 1200000, 600000, 1400000, 400000, 1600000, 200000, 300000, 1800000, 1200000, 800000, 400000]}

# Convert the data into a pandas dataframe
df = pd.DataFrame(data)

# Convert the first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
plt.figure(figsize=(10, 6))

# Set the x-axis and y-axis labels
plt.xlabel('Category')
plt.ylabel('Sales ($)')
plt.title('Retail and E-commerce Sales Comparison')

# Set the x-ticks and ticklabels
plt.xticks(range(len(df)), df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Set the y-ticks and ticklabels
# Calculate the max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up to the nearest multiple of 10, 100, or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value/10)*10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value/100)*100
else:
    max_total_value = np.ceil(max_total_value/1000)*1000
# Set the y-ticks
plt.yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot the data as an area chart
ax = plt.stackplot(range(len(df)), df['Retail Sales ($)'], df['E-commerce Sales ($)'], labels=['Retail Sales', 'E-commerce Sales'], colors=['#5E5E5E', '#FDB813'], alpha=0.7)

# Add grid lines
plt.grid(linestyle='--')

# Add legend
plt.legend(loc='upper left')

# Automatically resize the image
plt.tight_layout()

# Save the image as a png file
plt.savefig('output/final/area_chart/png/20231228-155112_11.png', bbox_inches='tight')

# Clear the current image state
plt.clf()