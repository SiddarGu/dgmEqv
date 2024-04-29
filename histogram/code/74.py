import matplotlib.pyplot as plt
import seaborn as sns

# Data provided
data_labels = ['Number of Visitors (Thousands)']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350']
data = [7, 12, 9, 3, 2, 1, 1]

# Create the figure and axis object
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Plotting the data in a vertical histogram
sns.barplot(x=line_labels, y=data, ax=ax, palette="viridis")

# Set the title and labels
ax.set_title('Visitor Turnout for Museum Exhibits')
ax.set_xlabel('Visitor Range')
ax.set_ylabel('Number of Museums')

# If the text length of the label is too long, rotate labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", wrap=True)

# Automatically adjust subplot params for a nice layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/74.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure
plt.clf()
