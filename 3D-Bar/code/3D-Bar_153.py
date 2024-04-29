import matplotlib.pyplot as plt
import numpy as np

# Define the dataset
dataset_text = "Year,Education Policy Funding ($ Billion),Public Health Funding ($ Billion),Environmental Policy Funding ($ Billion),Defense Policy Funding ($ Billion)\n 2018,120,80,200,250\n 2019,130,100,210,270\n 2020,140,120,230,280\n 2021,150,130,250,300"

# Split the data and convert to the appropriate format
lines = dataset_text.split('\n')
headers = lines[0].split(',')
rows = [line.split(',') for line in lines[1:]]

x_values = np.array([row[0] for row in rows])
y_values = np.array(headers[1:])
data = np.array([list(map(float, row[1:])) for row in rows])

# Create the figure and add a 3D subplot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plotting each column separately
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.8, data[:, i], color=plt.cm.viridis(i/len(y_values)), alpha=0.6)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')

# Adjusting view for better readability
ax.view_init(elev=20., azim=-35)

# Setting chart title and labels
ax.set_title('Comparative Funding Allocation for Key Government Policies (2018-2021)')
ax.set_xlabel('Year')
ax.set_ylabel('Policy')
ax.set_zlabel('Funding ($ Billion)')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/115_202312302126.png')
plt.clf()
