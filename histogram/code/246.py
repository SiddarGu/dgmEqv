import matplotlib.pyplot as plt

# Data parsing
data = """
Production Stage,Units Produced (thousands)
Raw Materials Processing,250
Component Assembly,198
Initial Quality Testing,180
Final Assembly,165
Packaging,140
Warehousing,123
Shipping,95
"""

# Transform the given data into three variables: data_labels, data, line_labels
lines = data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Create figure and axis for horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 8))

# Plotting the data
ax.barh(y=line_labels, width=data, align='center', color=plt.cm.viridis(range(len(data))))

# Title and labels
ax.set_title('Production Volume Through Various Manufacturing Stages')
ax.set_xlabel('Units Produced (thousands)')
ax.set_ylabel('Production Stage')

# Adding background grid
ax.grid(True)

# Rotating or wrapping long text if necessary
ax.set_yticklabels(line_labels, fontsize=8)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/246.png', format='png')

# Clear the current image state
plt.clf()
plt.close()
