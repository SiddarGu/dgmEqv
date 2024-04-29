import matplotlib.pyplot as plt
import squarify

# Given data in CSV-like string format
csv_data = """Healthcare Service,Percentage(%)
Preventive Care,18
Surgical Procedures,22
Emergency Services,15
General Consultation,20
Medication Prescription,10
Mental Health Services,8
Rehabilitation Services,5
Dental Services,2"""

# Split the data into lines and then into labels and values
lines = csv_data.split('\n')
data_labels = lines[0].split(',')[1:]  # Get the labels for the columns
line_labels = [line.split(',')[0] for line in lines[1:]] # Get the labels for the rows
data = [float(line.split(',')[1]) for line in lines[1:]] # Get the numerical data

# Set the figure size to prevent content from being displayed improperly.
plt.figure(figsize=(12, 8))

# Create the treemap
squarify.plot(sizes=data, label=line_labels, alpha=.7)

# Rotate the labels if needed and use wrap=True to ensure they fit well
for axis in plt.gcf().axes:
    for label in axis.get_xticklabels():
        label.set_rotation(45)  # Rotate labels if needed
        label.set_wrap(True)    # Wrap labels to prevent overlap
    
# Add the title
plt.title('Allocation of Healthcare Services by Type')

# Remove the axes
plt.axis('off')

# Resize the figure to fit all content
plt.tight_layout()

# Save the figure
output_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/229.png'
plt.savefig(output_path, format='png')

# Clear the current figure state to prevent interference with any further plots
plt.clf()
