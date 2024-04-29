
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

labels = ['Bachelor\'s Degree', 'Master\'s Degree', 'Doctorate Degree', 'Professional Certification', 'Professional Experience']
sizes = [25, 35, 25, 10, 5]
explode = [0, 0, 0, 0, 0]

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
ax.set_title('Educational Level Distribution of Science and Engineering Professionals in the USA, 2023')
ax.legend(labels, loc="upper right", bbox_to_anchor=(1, 0, 0.2, 1))
plt.xticks(rotation=-45)
plt.tight_layout()
plt.savefig("pie chart/png/406.png")
plt.clf()