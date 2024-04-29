
import matplotlib.pyplot as plt
plt.figure(figsize=(6,6))
labels = 'Music', 'Theatre', 'Visual Arts', 'Dance', 'Literature', 'Media Arts'
sizes = [21,17,22,15,15,10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6','#8d8d8d']
explode = (0,0,0,0,0,0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Distribution of Artforms in the USA, 2023')
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/222.png')
plt.clf()