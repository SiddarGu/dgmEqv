import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
        'Revenue Growth (%)': [6.5, 7.2, 8.0, 5.9]}
df = pd.DataFrame(data)

# Set the labels
data_labels = list(df.columns)[1:]  # labels of each column except the first column
line_labels = df['Quarter'].values  # labels of each row except the first row

# Create a figure and a horizontal bar plot
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Create horizontal bar plot
bars = plt.barh(line_labels, df['Revenue Growth (%)'], color=plt.cm.Paired.colors, edgecolor='black')

# Add grid, title and format the labels to avoid overlapping
plt.title('Quarterly Revenue Growth in the Finance Sector')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout to make space for labels
plt.tight_layout()

# Rotate x-tick labels if needed
for label in ax.get_xticklabels():
    label.set_rotation(45)
    label.set_ha('right')

# Save the plot as an image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/152.png'
plt.savefig(save_path)

# Clear the current image state
plt.clf()
