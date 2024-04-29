
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
ax = plt.subplot()
ax.bar(x=['USA','UK','Germany','France'], height=[250,200,230,220], width=0.3, bottom=0, label='Coal Production(TWh)', color='black')
ax.bar(x=['USA','UK','Germany','France'], height=[80,50,70,60], width=0.3, bottom=[250,200,230,220], label='Solar Production(TWh)', color='yellow')
ax.bar(x=['USA','UK','Germany','France'], height=[90,120,100,110], width=0.3, bottom=[330,250,300,280], label='Wind Production(TWh)', color='green')
ax.set_title('Energy production from Coal, Solar and Wind in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Energy Production(TWh)')
ax.legend()
rects=ax.patches
for rect, label in zip(rects, [250,200,230,220,80,50,70,60,90,120,100,110]):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height+5, label, ha='center', va='bottom')
plt.xticks(['USA','UK','Germany','France'])
plt.tight_layout()
plt.savefig('Bar Chart/png/412.png')
plt.clf()