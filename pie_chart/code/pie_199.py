
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot()

labels = ['Full-time Employees','Part-time Employees','Contract Workers','Interns']
sizes = [60, 20, 15, 5]
colors = ['lightskyblue', 'lightcoral','yellowgreen','gold']
explode = (0, 0, 0, 0.1)

ax.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_title('Employee Distribution in the USA, 2023', fontsize=14, fontweight='bold')
ax.axis('equal')

plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('pie chart/png/179.png')
plt.clf()