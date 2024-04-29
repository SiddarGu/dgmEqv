import matplotlib.pyplot as plt
import squarify

# Parsing the data
data_string = '''Health Category,Expenditure (%)
Hospital Care,38
Physician Services,25
Dental Services,7
Prescription Drugs,15
Nursing Home Care,5
Home Health Care,4
Medical Equipment,3
Over-the-counter Medicines,2
Other Health Services,1'''

# Processing the data to create required variables
lines = data_string.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Draw the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.7)

# Customize the plot
plt.title("Health Expenditure Distribution by Service Category")
plt.axis('off')

# Resize the image and save it
plt.tight_layout()
save_path = "/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1020.png"
plt.savefig(save_path, format='png')

# Clear the current figure state to prevent interference with future plots.
plt.clf()
