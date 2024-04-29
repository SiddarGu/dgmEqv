import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# given data
data_str = "Year,Healthcare Spending ($Bn),Education Spending ($Bn),Defense Spending ($Bn),Infrastructure Spending ($Bn)/n 2015,500,600,780,400/n 2016,550,800,900,450/n 2017,580,700,950,500/n 2018,600,900,1000,520/n 2019,650,950,1100,550"

# splitting the string to get the data
data_list = data_str.split("/n")

# assigning column labels and row labels
y_values = data_list[0].split(",")[1:]
x_values = [row.split(",")[0] for row in data_list[1:]]

# creating a 2D list for numerical data (using np.float32 for precision)
data = np.array([list(map(np.float32, row.split(",")[1:])) for row in data_list[1:]])

# creating a new figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# plotting each column of data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.4, data[:, i], shade=True, alpha=0.7)

# setting x-axis and y-axis labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# setting title
ax.set_title('Government Spending in Key Public Policy Areas (2015-2019)')

# adjusting view angle for better readability
ax.view_init(elev=20., azim=-35)

# save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/168_202312302235.png')

# clear the current image state
plt.clf()
