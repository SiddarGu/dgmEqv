import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# split the data
data_str = "Area,Civil Cases Filed,Criminal Cases Filed,Family Cases Filed,Corporate Cases Filed\nMetropolitan Area,2000,1500,1000,2500\nUrban Area,1800,1300,1200,2200\nSuburban Area,1500,1100,1400,1800\nRural Area,1200,900,800,1300"

# Prepare data
lines = data_str.split("\n")
y_values = lines[0].split(",")[1:]
x_values = [line.split(",")[0] for line in lines[1:]]
data_arr = np.array([line.split(",")[1:] for line in lines[1:]], dtype=np.float32)

# Empty figure
fig = plt.figure(figsize=(10, 10))

# Add subplot with 3D projection
ax = fig.add_subplot(111, projection='3d')

# Plot data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.4, 0.8, data_arr[:, i], color=np.random.rand(3,), alpha=0.8)
    
# Label the axis
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left')
plt.title("Distribution of Legal Cases by Area and Case Type")

# Adjust camera
ax.view_init(elev=50, azim=-50)

# Make sure everything fits
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/159_202312302235.png')

# Clear current figure
plt.clf()
