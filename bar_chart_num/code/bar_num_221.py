
import matplotlib.pyplot as plt
import numpy as np

Country=["USA","UK","Germany","France"]
Lawyers=[150,180,120,130]
Judges=[80,90,70,85]
Paralegals=[550,600,500,540]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

barWidth = 0.5
r1 = np.arange(len(Lawyers))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

ax.bar(r1, Lawyers, color='#4dac26', width=barWidth, edgecolor='white', label='Lawyers')
ax.bar(r2, Judges, color='#ffb000', width=barWidth, edgecolor='white', label='Judges')
ax.bar(r3, Paralegals, color='#984ea3', width=barWidth, edgecolor='white', label='Paralegals')

plt.xticks([r + barWidth for r in range(len(Lawyers))], Country)
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
plt.title("Number of legal professionals in four countries in 2021")
for i in range(len(Lawyers)):
    ax.annotate(Lawyers[i], xy=(r1[i],Lawyers[i]),rotation=0, ha='center', va='bottom',fontsize=8)
    ax.annotate(Judges[i], xy=(r2[i],Judges[i]),rotation=0, ha='center', va='bottom',fontsize=8)
    ax.annotate(Paralegals[i], xy=(r3[i],Paralegals[i]),rotation=0, ha='center', va='bottom',fontsize=8)
plt.tight_layout()
plt.savefig('Bar Chart/png/277.png')
plt.clf()