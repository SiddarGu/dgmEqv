import matplotlib.pyplot as plt

# Given data
data_labels = ['0.1-0.5', '0.5-1.0', '1.0-1.5', '1.5-2.0', '2.0-2.5', '2.5-3.0', '3.0-3.5', '3.5-4.0']
data = [12, 30, 25, 18, 10, 4, 2, 1]
line_labels = ['Revenue Bracket ($Billion)', 'Number of Companies']

# Create figure and subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot vertical histogram
bars = ax.bar(data_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Add grid
ax.yaxis.grid(True)

# Set title and labels
ax.set_title('Revenue Breakdown of Companies in the Food and Beverage Industry', fontsize=14)
ax.set_xlabel(line_labels[0], fontsize=12, wrap=True)
ax.set_ylabel(line_labels[1], fontsize=12)

# Handling label texts
plt.xticks(rotation=45, ha='right')

for bar in bars:
    height = bar.get_height()
    ax.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Automatically resize the image
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1012.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
