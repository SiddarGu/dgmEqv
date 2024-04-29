
import matplotlib.pyplot as plt
import numpy as np

data = {'Country':['USA','UK','Germany','France'],
        'Sports Teams':[20,30,25,27],
        'Sports Events':[50,60,55,58],
        'Viewers':[400000,450000,380000,400000]}

Country = data['Country']
Sports_Teams = data['Sports Teams']
Sports_Events = data['Sports Events']
Viewers = data['Viewers']

ind = np.arange(len(Country))
width = 0.2

fig, ax = plt.subplots(figsize=(15,8))
p1 = ax.bar(ind, Sports_Teams, width, color='#ffb6c1')
p2 = ax.bar(ind + width, Sports_Events, width, color='#87ceeb')
p3 = ax.bar(ind + width * 2, Viewers, width, color='#add8e6')

ax.set_title('Number of sports teams, events and viewers in four countries in 2021')
ax.set_xticks(ind + width)
ax.set_xticklabels(Country)

ax.legend((p1[0], p2[0], p3[0]), ('Sports Teams', 'Sports Events', 'Viewers'))
ax.autoscale_view()

for i, v in enumerate(Sports_Teams):
    ax.text(i, v + 2, str(v), color='#ffb6c1', fontweight='bold')
for i, v in enumerate(Sports_Events):
    ax.text(i + width, v + 2, str(v), color='#87ceeb', fontweight='bold')
for i, v in enumerate(Viewers):
    ax.text(i + width * 2, v + 2, str(v), color='#add8e6', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/19.png')
plt.clf()