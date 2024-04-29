import matplotlib.pyplot as plt
import squarify

# Given data in the specified format
data_str = """Health Aspect,Healthcare Spending (%)
Hospital Services,30
Prescription Medications,25
Physician Services,20
Clinical Services,15
Dental Services,5
Home Healthcare,3
Medical Equipment,2"""

# Transforming the data into required format
rows = data_str.strip().split('\n')
data_labels = rows[0].split(',')[1:]  # Extract data_labels (column labels)
line_labels = [row.split(',')[0] for row in rows[1:]]  # Extract line_labels (row labels)
data = [int(row.split(',')[1]) for row in rows[1:]]  # Extract numerical data

# Create the treemap
plt.figure(figsize=(12, 8))
colors = plt.cm.Spectral_r([float(value) / sum(data) for value in data])
print(colors)
squared= squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.6, edgecolor='w', linewidth=5)
for axis in ['top', 'bottom', 'left', 'right']:
    squared.spines[axis].set_linewidth(0)
# Squarify documentation suggest to use bar_kwargs to remove the edges as follows, setting linewidth to 0:
# squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.6, 
#               bar_kwargs={'edgecolor':'none', 'linewidth':0})

plt.title('Allocation of Healthcare Spending Across Health Services in 2023', fontsize=18)
plt.axis('off')  # Hide the axis

# Resize the figure to prevent content from being displayed
plt.tight_layout()

# Save the figure
saving_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/113.png'
plt.savefig(saving_path, format='png', dpi=300)

# Clear the current plot to free memory
plt.clf()
