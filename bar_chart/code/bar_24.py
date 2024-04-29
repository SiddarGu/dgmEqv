
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 400, 500],
        ['UK', 350, 450],
        ['Germany', 380, 420],
        ['France', 370, 480]]

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
x = np.arange(len(data))
width = 0.2
ax.bar(x, [i[1] for i in data], width, label='Sports')
ax.bar(x + width, [i[2] for i in data], width, label='Entertainment')
ax.set_title('Number of sports and entertainment events in four countries in 2021')
ax.set_xticks(x + width/2)
ax.set_xticklabels([i[0] for i in data], rotation=45, ha='right', wrap=True)
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/383.png')
plt.clf()