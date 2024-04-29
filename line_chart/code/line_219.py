
import matplotlib.pyplot as plt
import numpy as np

x = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'])
y1 = np.array([150, 170, 180, 200, 220, 240, 260, 280])
y2 = np.array([4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5])

fig = plt.figure(figsize=(11, 8), dpi=80)
ax = fig.add_subplot(111)
ax.plot(x, y1, color='b', linestyle='-', marker='o', markersize=8, label='Viewers (in millions)')
ax.plot(x, y2, color='r', linestyle='-', marker='o', markersize=8, label='Subscribers (in millions)')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=2)
ax.set_title("Monthly changes in viewers and subscribers for a video streaming service")
ax.set_xlabel('Month')
ax.set_xticks(x)
ax.set_xticklabels(x, rotation='vertical', fontsize=10)
ax.grid(True, linestyle='--', color='#F4F3F3', linewidth=1)
plt.tight_layout()
plt.savefig('line chart/png/277.png')
plt.clf()