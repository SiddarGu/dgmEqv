
import matplotlib.pyplot as plt
from matplotlib.patches import Shadow

labels = ['Full-time','Part-time','Contract','Intern']
sizes = [50,30,15,5]
colors = ['#FFD700','#F08080','#4682B4','#008000']
explode = (0.1,0,0,0)

fig, ax = plt.subplots(figsize=(10,10))
ax.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True)
ax.legend(labels,loc='upper right', bbox_to_anchor=(0.5, 0.5), shadow=True, fontsize=12)
ax.set_title('Employee Distribution in a Company, 2023', fontsize=14)
ax.text(-0.1, 0.5, 'Employee Type', fontsize=14, fontweight='bold', ha='center', va='center', rotation='vertical')

ax.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/502.png')
plt.clf()