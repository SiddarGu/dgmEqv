import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {
    "Employee Satisfaction Level": ["1-2 (Very Low)", "2-3 (Low)", "3-4 (Moderate)", "4-5 (High)", "5-6 (Very High)"],
    "Number of Companies": [3, 6, 15, 18, 8]
}

# Transform the given data into three variables
data_labels = list(data.keys())
line_labels = data[data_labels[0]]
data_values = data[data_labels[1]]

# Create a DataFrame
df = pd.DataFrame(data)

# Creating a figure and a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 8))

# Plotting with pandas .plot function
df.plot(kind='barh', x=data_labels[0], y=data_labels[1], ax=ax, legend=False, color='skyblue', edgecolor='black')

# Setting title and labels
ax.set_title('Company Distribution by Employee Satisfaction Levels')
ax.set_xlabel('Number of Companies')
ax.set_ylabel('Employee Satisfaction Level')

# Add grid
ax.grid(True, linestyle='--', alpha=0.7)

# Rotate x labels if too long
for tick in ax.get_xticklabels():
    tick.set_rotation(45)

# Set properties for y labels
ax.set_yticklabels(line_labels, rotation=0, wrap=True)

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Removing the grid behind the bars
ax.set_axisbelow(True)

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/124.png', bbox_inches='tight')

# Clear the current figure
plt.clf()
