import matplotlib.pyplot as plt
import pandas as pd
import os

# Data
data_labels = ['Annual Sales ($ Billion)']
line_labels = [
    'Snacks', 'Beverages', 'Dairy', 'Confectionery', 
    'Bakery', 'Meat & Poultry', 'Frozen Foods', 'Grains & Cereals'
]
data = [12.5, 20.3, 14.7, 7.4, 10.8, 17.9, 9.2, 13.5]

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Plot histogram
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
df.plot(kind='bar', ax=ax, color='skyblue', grid=True)

# Add labels and title
ax.set_xlabel('Product Category')
ax.set_ylabel('Annual Sales ($ Billion)')
ax.set_title('Annual Sales by Product Category in the Food and Beverage Industry')

# Rotate labels if necessary
ax.set_xticklabels(df.index, rotation=45, horizontalalignment='right', fontweight='light', fontsize='medium')

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Create directory for the output path if it doesn't exist
output_dir = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the figure
plt.savefig(f'{output_dir}/157.png', format='png')

# Clear the current figure's state after saving the image
plt.clf()
