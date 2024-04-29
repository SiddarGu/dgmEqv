
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Q1','Q2','Q3','Q4']
line_labels = ['Patient Outcomes','Research Quality','Care Quality','Patient Satisfaction','Cost Efficiency']
data = [[90,95,100,105],[80,85,90,95],[85,90,95,100],[75,80,85,90],[70,75,80,85]]

# Create figure before plotting
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Plot data
for i,row in enumerate(data):
    row = np.append(row,row[0])
    ax.plot(angles, row, color='C'+str(i), alpha=0.75, label=line_labels[i])
    ax.fill(angles, row, color='C'+str(i), alpha=0.15)

# Plot gridlines
for i in range(len(data)):
    ax.plot(angles, np.full_like(angles, (i+1)*np.max(data)/len(data)), color="grey", alpha=0.3)

# Plot axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14, ha='right', wrap=True)

# Adjust the radial limits
ax.set_ylim(0,np.max(data))

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Set title
plt.title('Healthcare Evaluation - 2021', fontsize=20)

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/17.png')

# Clear current image state
plt.cla()