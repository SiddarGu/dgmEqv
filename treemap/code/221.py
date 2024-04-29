import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Administration', 'Sales', 'Marketing', 'Human Resources', 'Operations', 'Research and Development', 'IT Services']
line_labels = ['Engagement Score (%)']
data = [15, 20, 15, 10, 20, 10, 10]

# Ensure enough space for the largest label
plt.figure(figsize=(12, 8))

# Plotting the treemap with the given data
squarify.plot(sizes=data, label=data_labels, color=None, alpha=0.8, text_kwargs={'wrap': True})

# Setting the title
plt.title('Employee Engagement Scores by Department in Human Resources Management')

# Tight layout to fit everything and prevent content cut-off
plt.tight_layout()

# Save the figure to the specified absolute path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/221.png')

# Clear the current figure state to prevent re-plotting the same figure
plt.clf()
