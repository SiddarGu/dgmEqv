import matplotlib.pyplot as plt
import numpy as np

data_string = '''Year,Internet Users (Millions),E-commerce Sales (Billion $),Number of Websites (Millions)
 2018,3050,8000,2000
 2019,3325,12000,2300
 2020,3500,22000,2600
 2021,3750,30000,2800
 2022,4000,35000,3100'''

lines = data_string.split("\n")
y_values = lines[0].split(",")[1:]
x_values = [line.split(",")[0] for line in lines[1:]]
data = np.array([list(map(float, line.split(",")[1:])) for line in lines[1:]], dtype=np.float32)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

xpos, ypos = np.meshgrid(range(len(x_values)), range(len(y_values)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(data.shape).flatten()

dx = dy = 0.8
dz = data.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

ax.set_xticks(range(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(range(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

ax.view_init(elev=20, azim=-45)

plt.title('Progression of Technology and Internet Usage 2018-2022')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/76_202312302126.png')
plt.clf()
