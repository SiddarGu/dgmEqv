import matplotlib.pyplot as plt
import squarify

# Given data
raw_data = """
Nonprofit Sector,Allocation (%)
Health Services,25
Education Services,20
Environmental and Wildlife Conservation,15
Human Rights Advocacy,12
Disaster Relief and Recovery,10
Arts and Culture,8
Scientific Research,5
Community Development,3
International Aid,2
"""

# Processing the raw data
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Create figure
plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=data, label=line_labels, alpha=0.7)

# Title and styling
plt.title('Allocation of Resources Among Charity and Nonprofit Organizations')
plt.axis('off')

# Resize and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/123.png', dpi=300)

# Clear the current image state at the end of the code
plt.clf()
