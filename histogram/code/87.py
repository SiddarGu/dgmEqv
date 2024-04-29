import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_labels = ["Monthly Occupancy Rate (%)", "Number of Hotels"]
line_labels = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]
data = [68, 72, 74, 78, 82, 80, 76, 79, 81, 85, 83, 70]

# Creating DataFrame
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[-1]])

# Creating figure and axes
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plotting the horizontal bar chart
df.plot(kind='barh', ax=ax, legend=False, color='skyblue')

# Setting the title, labels and grid
ax.set_title('Monthly Hotel Occupancy Rates Across the Industry')
ax.set_xlabel('Number of Hotels')
ax.set_ylabel('Months')
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Rotating labels if too long
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, wrap=True)

# Automatically adjust subplot params
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/87.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state to prevent reuse
plt.clf()
