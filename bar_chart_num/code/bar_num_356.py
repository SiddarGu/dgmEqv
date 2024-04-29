
import matplotlib.pyplot as plt
import numpy as np

Region = ['West', 'Midwest', 'South', 'East']
Houses = [300, 290, 280, 270]
Apartments = [400, 410, 420, 430]
Condominiums = [500, 520, 530, 540]

x = np.arange(len(Region))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(8, 6))
rects1 = ax.bar(x - width, Houses, width, label='Houses', color='#ADD8E6')
rects2 = ax.bar(x, Apartments, width, label='Apartments', color='#20B2AA')
rects3 = ax.bar(x + width, Condominiums, width, label='Condominiums', color='#FFA500')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Housing Units')
ax.set_title('Number of housing units in four regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Region)
ax.legend(loc='best')

# Add text for each bar
for rect in rects1:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')
for rect in rects2:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')
for rect in rects3:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/366.png')
plt.clf()