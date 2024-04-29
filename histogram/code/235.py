import matplotlib.pyplot as plt

# Given data
data_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81+']
data_values = [2.1, 1.8, 2.2, 2.5, 3.0, 3.8, 4.6, 5.2, 6.0]
line_labels = ['Average Hospital Visits per Year']

# Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot data
bars = plt.bar(data_labels, data_values, color=plt.cm.jet(range(len(data_values))), edgecolor='k')

# Add grid
plt.grid(axis='y', linestyle='--', linewidth=0.5)

# Add title and labels
plt.title('Average Hospital Visits Per Year by Age Group')
plt.ylabel('Average Visits')

# Customize x-axis labels
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right', wrap=True)

# Automatically adjust subplot params for the figure size
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/235.png'
plt.savefig(save_path)

# Clear the current figure state
plt.clf()
