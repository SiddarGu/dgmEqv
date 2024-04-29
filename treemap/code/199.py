import matplotlib.pyplot as plt
import squarify

# Given data
csv_data = """Department,Workforce Distribution (%)
Operations,25
Sales and Marketing,20
Human Resources,15
Research and Development,10
Information Technology,10
Customer Service,10
Finance and Accounting,5
Legal,3
Executive Management,2"""

# Parsing the CSV data
rows = csv_data.split('\n')

# Splitting CSV data into data_labels, line_labels and data
data_labels = rows[0].split(',')[1:]
line_labels = []
data = []
for row in rows[1:]:
    elements = row.split(',')
    line_labels.append(elements[0])
    data.append(float(elements[1]))

# Plotting the treemap
fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=.8)
plt.title('Workforce Distribution Across Departments in Corporate Structure')
plt.axis('off')

# Dealing with potentially long labels
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_horizontalalignment('right')
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/199.png'
plt.savefig(save_path, bbox_inches='tight')

# Clear the current figure's state to prevent interference with future plotting
plt.clf()
