import matplotlib.pyplot as plt
import numpy as np

raw_data = """Year,Number of Social Science Graduates,Number of Art Graduates,Number of Humanities Graduates/n 2018,3000,3500,4000/n 2019,3200,3700,4200/n 2020,3400,3900,4400/n 2021,3600,4100,4600/n 2022,3800,4300,4800"""
lines = raw_data.split("/n")
y_values = lines[0].split(",")[1:]
x_values = [line.split(",")[0] for line in lines[1:]]
data = np.array([list(map(int, line.split(",")[1:])) for line in lines[1:]], dtype = np.float32)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.7, data[:, i])

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

ax.set_title('NumberOf Graduates in Social Sciences, Arts and Humanities from 2018 to 2022')
ax.set_xlabel('Year')
ax.set_zlabel('Number of Graduates')
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/201_202312302235.png')
plt.clf()
