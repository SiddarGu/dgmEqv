
import matplotlib.pyplot as plt

labels = 'Primary School', 'Secondary School', 'Tertiary/Vocational School', 'University'
sizes = [25,35,25,15]
explode = (0, 0.1, 0, 0)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.set_title("Education Level Distribution in the USA, 2023", fontsize=14)
ax.axis('equal')

plt.tight_layout()
plt.xticks(fontsize=0)
plt.savefig('pie chart/png/468.png')
plt.clf()