

import matplotlib.pyplot as plt

labels = ['Mathematics', 'Computer Science', 'Physics', 'Chemistry', 'Biology', 'Mechanical Engineering', 'Electrical Engineering', 'Civil Engineering']
sizes = [20,25,15,15,15,5,5,5]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, rotatelabels=True)
ax.legend(loc="best", bbox_to_anchor=(1,1))
ax.set_title('Breakdown of Science and Engineering Fields in 2023')
plt.tight_layout()
fig.savefig('pie chart/png/462.png')
plt.clf()