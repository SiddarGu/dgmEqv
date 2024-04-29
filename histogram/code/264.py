import matplotlib.pyplot as plt

# Data preparation
data_labels = ['Number of Employees']
line_labels = ['Very Dissatisfied', 'Dissatisfied', 'Neutral', 'Satisfied', 'Very Satisfied']
data = [15, 30, 50, 80, 60]

# Create figure and add a subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot histogram
bars = ax.bar(line_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Add grid, title, and labels
ax.set_title('Employee Job Satisfaction Levels in Major Corporations', fontsize=16)
ax.set_xlabel('Job Satisfaction Level', fontsize=14)
ax.set_ylabel('Number of Employees', fontsize=14)
ax.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

# Rotate labels if they are too long
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# To prevent content from being displayed improperly
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/614.png'
plt.savefig(save_path)

# Clear the current figure state to prevent overlap in future plots
plt.clf()
