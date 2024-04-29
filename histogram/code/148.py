import pandas as pd
import matplotlib.pyplot as plt

# Given data transformed into variables
data_labels = ['Very High', 'High', 'Moderate', 'Low', 'Very Low']
line_labels = ['Number of Companies']
data = [12, 18, 25, 20, 5]

# Transforming the given data into a DataFrame
df = pd.DataFrame(data, index=data_labels, columns=line_labels)

# Creating a figure and adding subplots
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plotting the data as a histogram
df.plot(kind='bar', ax=ax, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], edgecolor='black')

# Customizing the plot
ax.set_title('Company Count Based on Employee Satisfaction Levels')
ax.set_xlabel('Employee Satisfaction Level')
ax.set_ylabel('Number of Companies')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust subplot params to give specified padding and prevent content from being clipped or overlapped
plt.tight_layout()

# Saving the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/148.png', format='png', dpi=300)

# Clearing the current image state
plt.clf()
