
import matplotlib.pyplot as plt
import numpy as np

data = [['Train',50,90],['Bus',30,100],['Car',60,60],['Bike',20,30]]

x_pos = np.arange(len(data))
costs = [cost[1] for cost in data]
times = [time[2] for time in data]

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
ax.bar(x_pos, costs, label='Average Cost', alpha=0.5, width=0.3)
ax.bar(x_pos + 0.3, times, label='Average Time', alpha=0.5, width=0.3)

ax.set_title('Average Cost and Time for Four Transportation Modes in 2021')
ax.set_xticks(x_pos)
ax.set_xticklabels([mode[0] for mode in data], rotation=45, ha='right')
ax.legend(bbox_to_anchor=(1,1), loc='upper left')

for i, v in enumerate(costs):
    ax.text(i-0.1, v+2, str(v), color='black', fontsize=12)
for i, v in enumerate(times):
    ax.text(i+0.2, v+2, str(v), color='black', fontsize=12)

plt.tight_layout()
plt.savefig('bar chart/png/157.png')
plt.clf()