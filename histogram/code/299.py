import pandas as pd
import matplotlib.pyplot as plt

# Define the provided data
data = [['25-34', 2600],
        ['35-44', 3200],
        ['45-54', 4500],
        ['55-64', 3500],
        ['65+', 1500]]

# Transform data into variables
data_labels = ['Age Group (Years)', 'Number of Physicians']
line_labels = [row[0] for row in data]  # Age groups
data_values = [row[1] for row in data]  # Number of Physicians

# Create a DataFrame
df = pd.DataFrame(data, columns=data_labels)

# Create a figure and add a subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot the data as a horizontal bar plot
df.plot(kind='barh', y='Number of Physicians', x='Age Group (Years)', ax=ax,
        legend=False, color=plt.cm.viridis(range(len(data_values))), alpha=0.7)

# Set the title and labels
ax.set_title('Distribution of Physicians by Age Group in the Healthcare Sector')
ax.set_xlabel('Number of Physicians')
ax.set_ylabel('Age Group (Years)')

# Rotate the x labels if they are too long
plt.xticks(rotation=45)
plt.yticks(range(len(line_labels)), line_labels, rotation=0)

# Optimize layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/649.png'
plt.savefig(save_path)

# Clear the current figure state
plt.clf()
