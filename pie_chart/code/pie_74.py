
import matplotlib.pyplot as plt
import numpy as np

labels = ['Civil Law','Criminal Law','Constitutional Law','Administrative Law','International Law','Contract Law']
sizes = [25,25,15,15,10,10]

fig = plt.figure(figsize=(14,10))
ax = fig.add_subplot(111)
ax.axis('equal')

explode = np.zeros(len(labels))
explode[0] = 0.1

ax.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',pctdistance=0.75,labeldistance=1.1,shadow=False)

plt.title("Distribution of Laws around the World, 2023", fontsize=20)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/506.png')
plt.clf()