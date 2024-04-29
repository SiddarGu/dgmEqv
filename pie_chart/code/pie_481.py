
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

labels = ['Male','Female']
sizes = [42, 58]
colors = ['#ff9999','#66b3ff']

ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal') 
plt.title('Gender Breakdown of Students at a University in 2023', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('pie chart/png/59.png')
plt.clf()