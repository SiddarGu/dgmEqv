
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

data = [['USA','Soccer',450],['UK','Cricket',400],['Germany','Hockey',380],['France','Basketball',420]]

x=np.arange(len(data))

bars = ax.bar(x, [i[2] for i in data], width=0.5, align='center', color='#3399FF', edgecolor='black', linewidth=1.2)

ax.set_title('Number of attendees for four sports in different locations in 2021',fontsize=14)
ax.set_ylabel('Attendees',fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels([i[0] for i in data], fontsize=12, rotation=45, wrap=True)

for bar,data in zip(bars,data):
    ax.annotate(data[2], xy=(bar.get_x() + bar.get_width() / 2, data[2]), xytext=(0, 3), 
                textcoords="offset points", ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.savefig('Bar Chart/png/587.png')
plt.clf()