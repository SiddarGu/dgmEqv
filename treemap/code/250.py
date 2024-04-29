import matplotlib.pyplot as plt
import squarify

# Data Preparation
raw_data = """
Transportation Type,Logistics Volume (%)
Road Freight,35
Ocean Shipping,25
Rail Transport,20
Air Freight,10
Pipeline,5
Intermodal,5
"""

# Splitting the data into lists and creating variables
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]

line_labels = []
data = []
for line in lines[1:]:
    label, value = line.split(',')
    line_labels.append(label)
    data.append(float(value))

# Creating the squarify plot
plt.figure(figsize=(12, 8))
colors = plt.cm.Spectral_r(range(len(data)))

squarify.plot(
    sizes=data, 
    label=[f"{label}\n{val}%" for label, val in zip(line_labels, data)], 
    color=colors, 
    alpha=0.7,
    pad=True
)

# Styling
plt.title('Distribution of Logistics Volume by Transportation Type')
plt.axis('off')

# Make the image more space-efficient
plt.tight_layout()

# Saving the image
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1047.png')

# Clear the current figure state
plt.clf()
