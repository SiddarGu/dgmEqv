
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

areas = ['Materials Science', 'Mechanical Engineering', 'Computer Science', 'Electrical Engineering', 'Civil Engineering', 
         'Chemical Engineering', 'Aerospace Engineering', 'Nanotechnology', 'Biomedical Engineering']
percentage = [20, 15, 25, 15, 10, 10, 5, 5, 5]

plt.figure(figsize=(8,8))
ax = plt.subplot()
ax.pie(percentage, labels=areas, startangle=90, autopct='%.1f%%', pctdistance=0.8, labeldistance=1.05, 
       textprops={'fontsize': 12, 'wrap': True, 'rotation': 90})

ax.set_title('Breakdown of Science and Engineering Fields in the US, 2023')
ax.legend(loc='upper left', bbox_to_anchor=(0.7, 0.9))
plt.tight_layout()
plt.savefig('pie chart/png/521.png', pad_inches=1, bbox_inches='tight')

plt.clf()