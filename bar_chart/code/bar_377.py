
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))
ax=plt.subplot(1,1,1)
ax.bar(x=['North America', 'South America', 'Europe', 'Asia'], height=[50, 60, 75, 80], width=0.5, label='Sports Teams', bottom=[0, 0, 0, 0], color='#1f77b4', edgecolor='black', linewidth=1)
ax.bar(x=['North America', 'South America', 'Europe', 'Asia'], height=[1000000, 920000, 800000, 700000], width=0.5, label='Fans', bottom=[50, 60, 75, 80], color='#ff7f0e', edgecolor='black', linewidth=1)
ax.set_title("Number of sports teams and their fans in four regions in 2021")
ax.set_ylabel('Number')
plt.xticks(rotation=45, ha='right')
plt.legend(loc=2, bbox_to_anchor=(1.05,1))
plt.tight_layout()
plt.savefig('bar chart/png/511.png')
plt.clf()