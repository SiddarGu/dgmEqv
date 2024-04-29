
import matplotlib.pyplot as plt

labels = ['Road', 'Rail', 'Air', 'Maritime']
sizes = [40, 15, 25, 20]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title("Distribution of Transportation Modes in the USA, 2023")
fig.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/24.png')
plt.clf()