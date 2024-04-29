import numpy as np
import matplotlib.pyplot as plt

# Data
data_str = """Year,Healthcare Policy Expenditure ($bn),Education Policy Expenditure ($bn),Defense Policy Expenditure ($bn)
2019,600,500,700
2020,650,550,750
2021,670,600,800
2022,680,630,900
2023,700,650,950"""

lines = data_str.split("\n")
headers = lines[0].split(",")
data_values = [list(map(np.float32, line.split(","))) for line in lines[1:]]

x_values = [line[0] for line in data_values]
y_values = headers[1:]
data = np.array([line[1:] for line in data_values])

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.4, 0.5, data[:, i], color=plt.cm.viridis(i / len(y_values)), alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.zaxis.set_rotate_label(False)

ax.set_title("Government Expenditure on Key Policies - 2019 to 2023", pad=40)

# Customize viewing angle and grids
ax.view_init(elev=22, azim=-50)
ax.grid(True)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/206_202312302235.png", dpi=150)
plt.close()
