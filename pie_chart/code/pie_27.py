
import matplotlib.pyplot as plt

labels = ['Male', 'Female']
sizes = [45, 55]
colors = ['#FFB6C1','#ADD8E6']
explode = (0.1, 0)

plt.figure(figsize=(7,7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=90)

plt.title('Gender Distribution in the USA, 2023', fontsize=20)
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/57.png')
plt.show()
plt.clf()