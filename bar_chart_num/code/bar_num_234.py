
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[200, 150, 450], 
                 [250, 180, 500], 
                 [220, 140, 400],
                 [230, 160, 470]])
x = np.arange(4)
country = ['USA', 'UK', 'Germany', 'France']

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.bar(x, data[:, 0], label='Music Events', bottom=data[:, 1]+data[:, 2])
ax.bar(x, data[:, 1], label='Theatre Performances', bottom=data[:, 2])
ax.bar(x, data[:, 2], label='Museum Visitors')
plt.xticks(x, country)
plt.title('Arts and Culture activities in four countries in 2021')
plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)

for i in range(len(x)):
    y_offset = 0
    for j in range(3):
        ax.annotate(str(data[i][j]), xy=(x[i], y_offset + 0.1), va='center', ha='center', fontsize=14, rotation=90)
        y_offset += data[i][j]
plt.tight_layout()
plt.savefig('Bar Chart/png/271.png')
plt.clf()