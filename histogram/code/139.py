import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_labels = ['Occupancy Rate (%)', 'Number of Hotels']
line_labels = ['Under 50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']
data = [
    [10], [18], [25], [22], [15], [5]
]

# Transforming the given data into a pandas DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels[1:])

# Create matplotlib figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot the data using horizontal bar chart
df.plot(kind='barh', ax=ax, legend=False, color='skyblue')

# Adding features to make the plot fancy
plt.title('Hotel Occupancy Rates Across Different Categories')
plt.xlabel(data_labels[1])
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Manage long label strings
ax.set_yticklabels(labels=line_labels, rotation=0, wrap=True)

# Automatically adjust subplot params for a nicer fit
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1008.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state to prevent overlap on future plots
plt.clf()
