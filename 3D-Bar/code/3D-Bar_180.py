import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parsing data
raw_data = """Year,Donations ($000),Number of Volunteers,Number of Beneficiaries
2019,1200,300,5000
2020,1500,350,6000
2021,1700,400,7000
2022,2000,450,7500
2023,2300,500,8000"""

# Replace /n with \n to escape newline characters
parsedData = raw_data.replace("/n", "\n").split("\n")
x_values = [row.split(',')[0] for row in parsedData[1:]]
y_values = parsedData[0].split(',')[1:]
data = np.array([[float(val) for val in row.split(',')[1:]] for row in parsedData[1:]])

# Creating figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
for c, i, y_value in zip(colors, range(len(y_values)), y_values):
    ax.bar(np.arange(len(x_values)), data[:, i], zs=i, zdir='y', color=c, alpha=0.8)

ax.set_xlabel('Year')
ax.set_yticklabels(y_values, ha='left')
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation = 45)
ax.set_title('Charitable Contributions, Volunteer Participation and Beneficiaries 2019 to 2023')

# Saving Figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/202_202312302235.png', format='png')

# Clear current figure
plt.clf()
