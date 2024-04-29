import matplotlib.pyplot as plt

# Given data transformed into three variables
data_labels = ['Annual Consumption (TWh)']
data = [
    [2400],
    [1800],
    [800],
    [900],
    [300],
    [250],
    [150]
]
line_labels = ['Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Wind', 'Solar', 'Biomass']

# Create figure and subplot for the histogram
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Create the horizontal bar chart
ax.barh(line_labels, [d[0] for d in data], color=plt.cm.tab20c.colors, edgecolor='black')

# Add grid, labels, and title
ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.set_xlabel(data_labels[0])
ax.set_title('Annual Energy Consumption by Source in the United States')

# Adjust the display of labels to handle long text
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the figure to the specified path and clear the plotting state
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/242.png')
plt.clf()
