import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_labels = ['Online Sales ($ Billion)']
line_labels = ['Electronics', 'Home & Furniture', 'Clothing & Apparel', 'Beauty & Health', 'Sports & Outdoors',
               'Books & Media', 'Food & Beverage', 'Toys & Hobby']
data = [78.5, 64.3, 90.2, 53.7, 47.1, 39.7, 86.9, 62.5]

# Creating DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Creating figure and axes instance
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Plotting histogram
df.plot(kind='bar', ax=ax, color='skyblue', grid=True)

# Setting the title
ax.set_title('Online Retail Sales Distribution by Product Category')

# Setting labels rotation to avoid overlapping
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# Adjust layout to fit everything cleanly
plt.tight_layout()

# Save the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/80.png', dpi=300)

# Clear the current figure state to prevent interference with future plots
plt.clf()
