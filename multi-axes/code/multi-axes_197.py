import matplotlib.pyplot as plt
import numpy as np

# Preparing the data
data_labels = ['Number of Beds', 'Number of Doctors', 'Number of Nurses', 'Average Patient Stay']
line_labels = ['Hospitals', 'Clinics', 'Outpatient Centers', 'Long-term Care Facilities', 'Rehabilitation Centers', 'Medical Laboratories']

data = np.array([
    [500, 150, 500, 5],
    [100, 50, 75, 2],
    [100, 30, 50, 1],
    [200, 20, 100, 10],
    [50, 10, 25, 4],
    [50, 5, 10, 0.5]
])

# Create figure
fig = plt.figure(figsize=(20,20))
ax1 = fig.add_subplot(111)

# Generate multiple bar charts
width = 0.15
ind = np.arange(len(data))
colors = ['b', 'g', 'r', 'c'] 

# Loop through the data and plot
for i in range(data.shape[1]):
    if i == 0:
        ax = ax1
    else:
        ax = ax1.twinx()
        ax.spines['right'].set_position(('outward', 50*(i-1)))
        
    if i==0: # Bar chart
        ax.bar(ind-width*(data.shape[1]-i-1), data[:,i], width,color=colors[i], label=data_labels[i])

    elif i==1: # Line chart
        ax.plot(ind, data[:,i], '-o', color=colors[i], label=data_labels[i])

    elif i==2: # Line chart
        ax.plot(ind, data[:,i], '-*', color=colors[i], label=data_labels[i])
        
    elif i==3: # Scatter chart
        ax.scatter(ind, data[:,i], color=colors[i], label=data_labels[i])
    
    ax.yaxis.set_label(data_labels[i])
    ax.yaxis.label.set_color(colors[i])
    ax.tick_params(axis='y', colors=colors[i])
    ax.legend(loc=['upper left', 'upper right', 'upper center', 'lower left', 'center right'][i])

ax1.set_xticks(ind)
ax1.set_xticklabels(line_labels, rotation=45)
ax1.set_xlabel('Categories')
ax1.set_ylabel(data_labels[0])


# Set chart title
plt.title('Healthcare Facilities and Staffing Analysis')

# Automatically resize the image
plt.tight_layout()

# Save as png image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/311_202312311430.png")

# Clear figure to prevent overlaping plots
plt.clf()
