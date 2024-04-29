
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111)

fields = ['Computer Science', 'Mechanical Engineering', 'Electrical Engineering', 'Civil Engineering', 'Chemical Engineering', 'Biomedical Engineering']
percentages = [40, 15, 20, 10, 10, 5]

ax.pie(percentages, labels=fields, autopct='%1.1f%%', startangle=90, textprops={'fontsize':14}, wedgeprops={'linewidth': 1.5, 'edgecolor': 'white'})
ax.set_title('Distribution of Engineering Fields in the USA in 2023', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/404.png')
plt.clf()