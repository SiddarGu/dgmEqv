import matplotlib.pyplot as plt
import squarify

# Data provided in the question
data_string = "Category,Percentage (%)\n Recruitment,18\n Employee Training,20\n Performance Evaluation,15\n Compensation & Benefits,22\n Workforce Diversity,10\n Employee Relations,9\n Health & Safety,6"

# Parsing data
lines = data_string.strip().split('\n')
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0].strip() for line in lines[1:]]
data_values = [int(line.split(",")[1].strip()) for line in lines[1:]]

# Prepare data for plotting
data = data_values
sizes = data
label = ["{}\n{:.1f}%".format(label, value) for label, value in zip(line_labels, data)]

# Plotting with squarify
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=label, alpha=0.6)

# Setting title of the figure
plt.title('Allocation of HR Resources Across Employee Management Areas', fontsize=18)

# Improving layout and aesthetics
plt.axis('off')
plt.tight_layout()

# Save the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/81.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clearing the current figure state to prevent any overlapping of figures
plt.clf()
