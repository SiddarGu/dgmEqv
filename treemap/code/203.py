import matplotlib.pyplot as plt
import squarify

# Given data in raw format
raw_data = "Healthcare Area,Expenditure (%)\n Public Health Services,25\n Hospital Care,30\n Prescription Drugs,15\n Private Clinics,10\n Mental Health Services,10\n Dental Services,5\n Long-Term Care,4\n Medical Research,1"

# Processing the data to separate into labels and values
lines = raw_data.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0].strip() for line in lines[1:]]
data = [float(line.split(",")[1].strip()) for line in lines[1:]]

# Define colors for each segment (this can be customized to any color scheme you want)
colors = plt.cm.Spectral(range(len(data)))

# Create figure
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8, text_kwargs={'fontsize':12, 'wrap':True})

# Title setup with a larger fontsize
plt.title('Healthcare Expenditure Distribution across Different Services', fontsize=18)

# Removing the axes
plt.axis('off')

# Use tight_layout to automatically adjust subplot params to give the figure the exact layout to minimize unnecessary paddings
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/203.png', bbox_inches='tight', format='png', dpi=300)

# Clear the current figure state to prepare for any further plotting
plt.clf()
