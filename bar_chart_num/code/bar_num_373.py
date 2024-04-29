
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 320, 290], 
        ['UK', 60, 50], 
        ['Germany', 87, 77], 
        ['France', 70, 62]]

Country, Internet_Users, Social_Media_Users = np.array(data).T

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

width = 0.3
x_pos = np.arange(len(Country))

rects1 = ax.bar(x_pos - width/2, Internet_Users, width, label='Internet Users', color='green')
rects2 = ax.bar(x_pos + width/2, Social_Media_Users, width, label='Social Media Users', color='blue')

ax.set_title('Number of internet and social media users in four countries in 2021')
ax.set_xticks(x_pos)
ax.set_xticklabels(Country)
ax.legend()

ax.autoscale_view()
ax.grid(True, axis='y')

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom',
                    bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.5),
                    rotation=0, wrap=True)

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.savefig('Bar Chart/png/461.png')
plt.clf()