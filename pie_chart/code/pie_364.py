
import matplotlib.pyplot as plt

labels = ['Music','Visual Arts','Theater','Literature','Film']
sizes = [30, 25, 15, 20, 10]
explode = (0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, textprops={'fontsize': 10, 'wrap': True, 'rotation': 45})
ax.axis('equal')
ax.set_title("Distribution of Art Forms in the United States, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/360.png')
plt.clf()