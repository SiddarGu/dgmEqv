
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

labels=['Mathematics','Computer Science','Engineering','Physics','Chemistry']
sizes=[25,20,35,15,5]
explode=[0.1,0,0,0,0]

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax.axis('equal') 
ax.set_title('Distribution of Science and Engineering Disciplines in Higher Education, 2023', fontsize=14)

plt.legend(labels, loc="best", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig('pie chart/png/62.png', bbox_inches='tight')
plt.clf()