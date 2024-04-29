
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Crops = [100, 80, 90, 110]
Livestock = [200, 150, 180, 210]
Fruit = [300, 250, 230, 270]

x = np.arange(len(Country))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(8,6))
rects1 = ax.bar(x - width, Crops, width, label='Crops')
rects2 = ax.bar(x, Livestock, width, label='Livestock')
rects3 = ax.bar(x + width, Fruit, width, label='Fruit')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Quantity (tons)')
ax.set_title('Agricultural production of crops, livestock and fruit in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend()

# label each bar with its respective value
for rect in rects1:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
for rect in rects2:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
for rect in rects3:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

fig.tight_layout()

plt.savefig('Bar Chart/png/2.png', dpi=100, bbox_inches='tight')

plt.clf()