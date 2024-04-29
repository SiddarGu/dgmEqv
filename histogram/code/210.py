import matplotlib.pyplot as plt
import os

# Given data
data = [
    [1500.5],
    [1800.7],
    [1200.3],
    [130.4],
    [60.2]
]
data_labels = ['Annual CO2 Emissions (Million Metric Tons)']
line_labels = ['Coal', 'Petroleum', 'Natural Gas', 'Renewables', 'Nuclear']

# Creating figure and histogram
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting the data
ax.bar(line_labels, [d[0] for d in data], color=['red', 'green', 'blue', 'yellow', 'purple'])

# Setting the title
ax.set_title('Carbon Dioxide Emissions by Energy Source')

# Adding grid
ax.grid(True)

# Setting x-axis labels
ax.set_xticklabels(line_labels, rotation=45, ha='right', wrap=True)

# Automatically adjust the display layout to prevent content from being cut
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/210.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clearing the current figure's state
plt.clf()
