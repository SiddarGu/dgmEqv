
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
 
labels = 'Civil Law', 'Criminal Law', 'Administrative Law', 'Constitutional Law', 'International Law', 'Human Rights Law', 'Contract Law'
sizes = [30, 20, 15, 10, 10, 10, 5]
colors = ['#FFC125', '#C0C0C0', '#DAA520', '#006400', '#0000CD', '#FF6347', '#8B4513']
explode = (0.1, 0, 0, 0, 0, 0, 0)

ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
ax.set_title('Distribution of Legal Areas in the USA in 2023', fontsize=15, fontweight='bold')
ax.legend(labels=labels, bbox_to_anchor=(1, 0.7), loc="upper right")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('pie chart/png/408.png')
plt.clf()