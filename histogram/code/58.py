import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_labels = ['Budget Allocation ($ Billion)']
line_labels = ['Education', 'Healthcare', 'Defense', 'Social Security', 'Infrastructure', 'Research and Development', 'Environmental Protection', 'Agriculture']
data = [15.5, 20.3, 32.8, 25.4, 17.7, 13.2, 9.6, 8.5]

# Create a DataFrame
df = pd.DataFrame(data=data, index=line_labels, columns=data_labels)

# Create a figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot the data
df.plot(kind='barh', ax=ax, color='skyblue', grid=True)

# Set the title
plt.title('Budget Allocation Across Different Policy Areas')

# Set text properties
plt.xlabel(data_labels[0])
plt.ylabel('Policy Areas')
plt.legend().set_visible(False)

# Handle the long text in the labels
ax.tick_params(axis='y', labelrotation=45)
ax.tick_params(axis='y', labelsize=8)

# Set tight layout to automatically adjust subplot params
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_val/58.png', format='png')

# Clear the current figure state
plt.clf()
