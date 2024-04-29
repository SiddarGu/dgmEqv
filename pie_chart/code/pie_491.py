
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,7))
labels = 'High School', 'College', 'Post-Graduate', 'Vocational'
sizes = [25, 45, 20, 10]
colors = ['#FFB6C1', '#FFC0CB', '#FF69B4', '#FF1493']
explode = (0, 0.1, 0, 0)

ax1 = fig.add_subplot()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 

plt.title('Education Level Distribution in the USA, 2023', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig("pie chart/png/296.png")

plt.clf()