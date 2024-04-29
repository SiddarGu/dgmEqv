
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(111)

labels = ['Automotive', 'Textile', 'Electronics', 'Metallurgy', 'Chemical', 'Woodworking', 'Plastic']
sizes = [15, 10, 25, 15, 20, 10, 15]

ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
ax1.set_title("Distribution of Manufacturing Sectors in the USA, 2023")
plt.legend()
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/373.png')
plt.clf()