import matplotlib.pyplot as plt
import numpy as np

# Data Labels and Variables
data_labels=["Yield Q1","Yield Q2","Yield Q3","Yield Q4"]
data= [[320, 370, 420, 490], 
       [370, 420, 470, 530], 
       [290, 340, 390, 450], 
       [450, 500, 550, 610], 
       [400, 450, 500, 560]]
line_labels= ["Wheat","Corn","Soya","Potatoes","Rice"]

# Create Radar chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True) 

# Interpolate angles for data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Loop through data and plot radar lines
for idx, d in enumerate(data):
    
    # Append first element to create closed line
    v = np.append(d, d[0])
    ax.plot(angles, v, label=line_labels[idx])
        
    # Generate and plot radius vector
    r = np.full_like(angles, (idx+1) * max(map(max, data)) / len(data))
    ax.plot(angles, r, color='grey', linestyle='dashed')

# Grids and Labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, [label.replace(" ", "\n") for label in data_labels])
ax.set_rlim(0, max(map(max, data)))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i / 1.5 for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=30)

# Legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Title
plt.title("Agriculture Yield - Quarterly")

# Remove polar gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Save and clear figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/111_2023122292141.png")
plt.clf()
