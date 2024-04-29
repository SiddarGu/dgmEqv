import matplotlib.pyplot as plt
import squarify

# Given data as string, to be transformed into 'data_labels', 'data', 'line_labels'
data_str = """HR Category,Percentage (%)
Recruitment,25
Training & Development,20
Performance Management,15
Compensation & Benefits,15
Employee Relations,10
Diversity & Inclusion,5
Health & Safety,5
Workforce Analytics,3
Compliance,2"""

# Parse the data into lists
data_lines = data_str.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [float(line.split(',')[1]) for line in data_lines[1:]]

# Create a figure and a corresponding axes
plt.figure(figsize=(12, 8))
ax = plt.gca()

# Plotting the treemap
squarify.plot(sizes=data, label=line_labels, text_kwargs={'fontsize':12, 'wrap':True})

# Set the title for the chart
plt.title('Proportions of Human Resource Management Efforts by Category', fontsize=16)

# Removing axis lines and labels
plt.axis('off')

# Adjust layout to make sure the content fits well
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1036.png'
plt.savefig(save_path, bbox_inches='tight')

# Clear the current figure state
plt.clf()
