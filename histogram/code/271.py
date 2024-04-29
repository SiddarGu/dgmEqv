import pandas as pd
import matplotlib.pyplot as plt

# Data
data_labels = ['Sales Volume (million units)']
line_labels = [
    'Soft Drinks',
    'Alcoholic Beverages',
    'Bottled Water',
    'Snack Foods',
    'Confectionery',
    'Dairy Products',
    'Frozen Foods',
    'Canned Goods'
]
data = [125.5, 95.0, 110.0, 89.7, 76.3, 105.2, 58.9, 51.4]

# Creating a DataFrame from the provided data
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create figure and add subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Plotting the data
df.plot(kind='bar', color='skyblue', edgecolor='black', ax=ax)

# Setting the title and labels
plt.title('Sales Volume Across Food and Beverage Categories')
plt.ylabel('Sales Volume (million units)')
plt.xlabel('Product Category')

# Add grid
plt.grid(axis='y')

# Set rotation for the x-tick labels if too long
plt.xticks(rotation=45, ha='right')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/621.png')

# Clear the current image state
plt.clf()
