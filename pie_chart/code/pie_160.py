
import matplotlib.pyplot as plt

Areas=['Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Chemical Engineering']
Percentage=[45, 20, 15, 10, 10]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.pie(Percentage, labels=Areas, autopct='%.2f%%', textprops={'fontsize':13, 'wrap':True, 'rotation':30})
plt.title("Distribution of Engineering Disciplines in Academic Research, 2023")
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/516.png')
plt.clf()