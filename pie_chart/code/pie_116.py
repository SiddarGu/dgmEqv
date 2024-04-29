
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
labels = ['Training and Development', 'Recruitment and Selection', 'Performance Management', 'Employee Relations',
          'Compensation and Benefits', 'Human Resource Planning', 'Health and Safety']
percentage = [22, 20, 16, 14, 14, 10, 4]
explode = (0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2)
ax.pie(percentage, explode=explode, labels=labels, autopct='%.2f%%', shadow=True, startangle=90, textprops={'fontsize': 14, 'wrap': True})
ax.axis('equal')
ax.set_title('Distribution of Human Resources Management Areas in the US, 2023', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.xticks(ticks=())
fig.savefig('pie chart/png/166.png', bbox_inches='tight')
plt.clf()