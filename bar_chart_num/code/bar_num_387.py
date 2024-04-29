
import matplotlib.pyplot as plt
import numpy as np

region = ['East', 'West', 'North', 'South']
breakfast = [100, 120, 150, 110]
lunch = [250, 220, 200, 300]
dinner = [400, 450, 380, 420]

x = np.arange(len(region))
width = 0.2

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(x - width, breakfast, width, label='Breakfast')
ax.bar(x, lunch, width, label='Lunch')
ax.bar(x + width, dinner, width, label='Dinner')

ax.set_xticks(x)
ax.set_xticklabels(region)
ax.set_title('Number of meals served in four regions in 2021')
ax.legend()
ax.autoscale_view()

for i in np.arange(len(x)):
    for j in np.arange(3):
        yvalue = [breakfast[i], lunch[i], dinner[i]][j]
        ypos = [breakfast[i], lunch[i] + breakfast[i], dinner[i] + lunch[i] + breakfast[i]][j]
        ax.annotate('{}'.format(yvalue), xy=(x[i], ypos), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/234.png')
plt.clf()