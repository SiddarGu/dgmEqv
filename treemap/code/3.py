import matplotlib.pyplot as plt
import squarify

# Transform given data into variables for charting
data_labels = ["Recruitment", "Training and Development", "Compensation and Benefits",
               "Employee Relations", "Health and Safety", "Performance Management",
               "Workforce Analytics", "Diversity and Inclusion"]
line_labels = ["Percentage (%)"]
data = [20, 15, 25, 10, 10, 10, 5, 5]

# Choose some nice colors for the treemap
colors = plt.cm.Dark2(range(len(data)))

# Create a figure with a predefined size to ensure the content fits well
fig, ax = plt.subplots(1, figsize=(12, 8))

# Create treemap with squarify
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.7)

# Decoration
plt.title("Human Resources Management: Distribution of Core Functions", fontsize=16, weight="bold")
plt.axis('off')

# Resize image
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/3.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state to avoid overlapping of multiple plots
plt.clf()
