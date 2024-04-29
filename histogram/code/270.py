import matplotlib.pyplot as plt

# Given data
data_labels = ['Theft', 'Assault', 'Drug Offenses', 'Fraud', 'Homicide', 'Burglary', 'Arson', 'Cybercrime']
data = [350, 280, 220, 170, 120, 95, 75, 65]
line_labels = ['Number of Cases']

# Create figure and axis
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Plot the histogram
bars = ax.bar(data_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Cases')
ax.set_title('Types of Legal Cases Handled in 2023')
ax.set_xticks(range(len(data_labels)))
ax.set_xticklabels(data_labels, rotation=45, ha='right', wrap=True)

# Draw grid lines behind the bars
ax.yaxis.grid(True)

# Set background color
ax.set_facecolor('lightgrey')

# Automatically resize the plot
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/620.png'
plt.savefig(save_path, format='png', dpi=300, bbox_inches='tight')

# Clear the current image state
plt.clf()
