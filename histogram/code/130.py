import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_str = "Quarter,Revenue Growth (%)\nQ1,5.2\nQ2,4.6\nQ3,4.9\nQ4,5.5"

# Transform data into required variables
rows = data_str.split('\n')
data_labels = rows[0].split(',')[1:]  # Skip the first label 'Quarter'
line_labels = [row.split(',')[0] for row in rows[1:]]
data = [float(row.split(',')[1]) for row in rows[1:]]

# Create a figure and a horizontal bar plot
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create horizontal bar plot using seaborn
sns.barplot(x=data, y=line_labels, palette='viridis')

# Set title and adjust layout
ax.set_title('Quarterly Revenue Growth in the Financial Sector')
plt.xlabel('Revenue Growth (%)')
plt.ylabel('Quarter')
plt.xticks(rotation=45, ha='right')

# Ensure grid is displayed
ax.yaxis.grid(True)

# Make sure all labels are displayed clearly
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/130.png'
plt.savefig(save_path)

# Clear the current figure state to prevent interference with any subsequent plots
plt.clf()
