import matplotlib.pyplot as plt
import pandas as pd

# Given data to three variables
data_labels = ['Yearly Sales ($Million)']
line_labels = [
    'Alcoholic Beverages', 'Non-Alcoholic Beverages', 'Packaged Foods',
    'Fresh Foods', 'Confectionery & Snacks', 'Dairy Products',
    'Meat & Poultry', 'Seafood'
]
data = [
    [125.3],
    [93.5],
    [150.4],
    [88.7],
    [97.8],
    [110.2],
    [134.9],
    [79.4]
]

# Create a Pandas DataFrame
df = pd.DataFrame(data, columns=data_labels, index=line_labels)

# Create a figure object and an axes object
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Create histogram using pandas plot function
df.plot(kind='bar', ax=ax, legend=False)
ax.set_title('Annual Sales in the Food and Beverage Industry by Product Type')
ax.set_xlabel('Product Type')
ax.set_ylabel('Yearly Sales ($Million)')
ax.grid(True)

# Improve layout, add rotation to x-axis labels, and handle long labels
plt.xticks(rotation=45, ha="right", wrap=True)

# Apply tight_layout to auto-adjust plot parameters to fill the figure
plt.tight_layout()

# Save the figure
output_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/200.png'
plt.savefig(output_path, dpi=300)

# Clear the current image state
plt.clf()
