
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(9,6))
width = 0.35
ax.bar(['USA','UK','Germany','France'], [600,400,500,450], width, label='Lawyers(thousands)', color='purple')
ax.bar(['USA','UK','Germany','France'], [90,100,120,110], width, label='Judges(thousands)', color='orange', bottom=[600,400,500,450])
ax.set_title('Number of lawyers and Judges in four countries in 2021')
ax.set_xticks(['USA','UK','Germany','France'])
ax.legend()
for i, v in enumerate([600,400,500,450]):
    ax.text(i-.12, v/2 + max([90,100,120,110])/2, str(v), color='blue', fontweight='bold')
for i, v in enumerate([90,100,120,110]):
    ax.text(i-.12, v/2 + 600, str(v), color='green', fontweight='bold')
plt.tight_layout()
plt.savefig('Bar Chart/png/97.png')
plt.clf()