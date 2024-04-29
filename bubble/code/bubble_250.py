import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Process data
raw_data = "Health Condition,Number of Diagnoses (Millions),Healthcare Expenditure (Billion $),Average Lifespan (Years),Quality Life Years (Score) " \
            "\n Heart Disease,30,200,70,7.5 " \
            "\n Cancer,20,220,65,6 " \
            "\n Diabetes,50,180,72,7 " \
            "\n Asthma,8,30,75,8 " \
            "\n Alzheimer's,6,100,80,6.5 " \
            "\n Arthritis,40,50,76,6.8"
raw_data = raw_data.split('\n')
data_labels = raw_data[0].split(',')[1:]
line_labels = []
data = []
for line in raw_data[1:]:
    elements = line.split(',')
    line_labels.append(elements[0] + elements[3])
    data.append([float(x) for x in elements[1:]])
data = np.array(data)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Create color normalizer
c_norm = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))

# Plot each point
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2]*50, c=data[i, 3], cmap='viridis', norm=c_norm, label=None)
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_labels[i])

ax.legend(title=data_labels[2], loc='upper left')

# Create colorbar
sm = ScalarMappable(norm=c_norm, cmap='viridis')
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Set title and labels
plt.title('Health Conditions Impact on Healthcare Expenditure and Lifespan')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

# Save figure 
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/294_202312310045.png')

# Clear figure
plt.clf()
