import matplotlib.pyplot as plt

# Given data
data_labels = ['Number of Daily Visits (Millions)']
line_labels = ['5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50']
data = [12, 20, 30, 22, 14, 7, 4, 3, 2]

# Creating the figure and the horizontal bar chart
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plotting the data
ax.barh(line_labels, data, color=plt.cm.tab20c.colors)

# Adding grid, title, and labels
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.title('Daily Website Traffic on Popular Social Media Platforms')
plt.xlabel(data_labels[0])

# Setting rotation for the x-tick labels if they are too long
plt.xticks(rotation=45, ha='right')

# Adjusting layout for the figure
plt.tight_layout()

# Saving the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/642.png'
plt.savefig(save_path, format='png', dpi=300)

# Clearing the current figure's state to prevent interference with further plots
plt.clf()
