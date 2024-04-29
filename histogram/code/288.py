import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Housing Price Range (Thousands USD)': [
        '100-200', '200-300', '300-400', '400-500', '500-600', '600-700', '700-800',
        '800-900', '900-1000', '1000-1100', '1100-1200'
    ],
    'Number of Houses Sold': [120, 215, 195, 165, 140, 95, 80, 60, 45, 30, 20]
}

# Transforming data into three variables
data_labels = ['Number of Houses Sold']
line_labels = data['Housing Price Range (Thousands USD)']
data_values = data['Number of Houses Sold']

# Create a pandas DataFrame
df = pd.DataFrame(data={'Number of Houses Sold': data_values}, index=line_labels)

# Create a figure with a larger size to avoid overlapping labels
plt.figure(figsize=(10, 8))

# Add a subplot for the horizontal bar chart
ax = plt.subplot()

# Create horizontal bar plot and add grid
df.plot(kind='barh', ax=ax, grid=True, edgecolor='black', color='skyblue')

# Set the title of the plot
plt.title('Sales Distribution Across Housing Price Ranges')

# Set rotation for the xticks if necessary
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/638.png'
plt.savefig(save_path, format='png')

# Clear the current figure state to prevent overlapping with future plots
plt.clf()
