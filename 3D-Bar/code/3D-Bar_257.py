import matplotlib.pyplot as plt
import numpy as np

data = """Year,Civil Cases (in thousands),Criminal Cases (in thousands),Family Cases (in thousands),Commercial Cases (in thousands)
2016,200,220,180,240
2017,210,230,190,260
2018,220,240,200,270
2019,230,250,210,280
2020,240,270,220,290"""

lines = data.split("\n")

y_values = lines[0].split(",")[1:]
x_values = [line.split(",")[0] for line in lines[1:]]

numeric_values = [list(map(float, line.split(",")[1:])) for line in lines[1:]]
data = np.array(numeric_values).astype(np.float32)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), np.array([i]*len(x_values)), np.zeros(len(x_values)), 0.4, 1, data[:, i], color=colors[i])

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left')

plt.title('Analysis of Legal Cases by Category from 2016 to 2020')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/277_202312310050.png')
plt.close()
