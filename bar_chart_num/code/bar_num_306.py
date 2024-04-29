
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[90,10],[80,20],[70,30],[60,40]])

xlabels = ["Experiment1", "Experiment2", "Experiment3", "Experiment4"]
x = np.arange(len(xlabels)) 

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(x, data[:,0], label="Success Rate (%)", bottom=data[:,1], width=0.5)
ax.bar(x, data[:,1], label="Fail Rate (%)", width=0.5)
ax.set_title("Success and Fail Rates of four Science and Engineering Experiments in 2021")
ax.set_xticks(x)
ax.set_xticklabels(xlabels)
ax.tick_params(labelsize=10)
ax.legend(loc='upper left', fontsize=10)

for x, y1, y2 in zip(x, data[:,0], data[:,1]):
    ax.annotate('{}%'.format(y1), xy=(x, y1/2+y2/2), va='center', ha='center', fontsize=10)
    ax.annotate('{}%'.format(y2), xy=(x, y2/2), va='center', ha='center', fontsize=10)

plt.tight_layout()
plt.savefig("Bar Chart/png/115.png")
plt.clf()