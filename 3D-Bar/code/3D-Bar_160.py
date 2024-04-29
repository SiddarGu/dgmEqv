import numpy as np
import matplotlib.pyplot as plt

raw_data = '''New York,1200,700,250
Los Angeles,900,650,230
Chicago,800,550,200
Houston,900,525,180
Phoenix,750,500,170'''
lines = raw_data.split('\n')

x_values = [line.split(',')[0] for line in lines]
y_values = ['New Home Sales (Units)', 'Housing Prices ($000)', 'Rent Prices ($000)']
data = np.array([line.split(',')[1:] for line in lines], dtype=np.float32)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

bar_width = 0.1
x_tick_locations = np.arange(len(x_values))

for i in range(len(y_values)):
    ax.bar3d(x=x_tick_locations, y=[i]*len(x_values), z=np.zeros_like(data[:,i]),
              dx=bar_width , dy=0.3, dz=data[:, i],
              color="b", alpha=0.6)

ax.view_init(elev=25, azim=-60)
ax.grid(True)

ax.set_xticks(x_tick_locations)
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation = 45, ha="right")
ax.set_yticklabels(y_values, rotation = 0, ha="left")
ax.view_init(elev=25, azim=165)

plt.title('Comparative Housing Market Analysis of US Cities', fontsize=16, pad=20)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/249_202312310050.png')
plt.cla()
plt.clf()
plt.close()
