import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Price Range (Thousands)': [
        '100-200', '200-300', '300-400', '400-500', '500-600',
        '600-700', '700-800', '800-900', '900-1000', '1000-1100'
    ],
    'Number of Houses Sold': [342, 410, 506, 321, 280, 165, 115, 88, 46, 22]
}

# Transform data into variables
data_labels = list(data.keys())
line_labels = data['Price Range (Thousands)']
data_values = data['Number of Houses Sold']

# Create DataFrame
df = pd.DataFrame(data, columns=data_labels)

# Create figure and subplot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot horizontal histogram
df.plot(kind='barh', x=data_labels[0], y=data_labels[1], ax=ax, color='skyblue', edgecolor='black')

# Set title and labels
ax.set_title('Sales Volume Distribution Across Different Housing Price Ranges', pad=20)
ax.set_xlabel('Number of Houses Sold')
ax.set_ylabel('Price Range (Thousands)')

# Set rotation for the x-axis labels if they overlap
plt.xticks(rotation=45)

# Add grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Wrap the labels if they are too long
ax.tick_params(axis='y', labelsize=10)
ax.set_yticklabels(line_labels, wrap=True)

# Adjust the layout to prevent content from being cut off
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/627.png')

# Clear the current figure's state
plt.clf()
