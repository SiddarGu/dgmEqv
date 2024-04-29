
import matplotlib.pyplot as plt

labels = ["Computers", "Smartphones", "Tablets", "TV", "Other"]
sizes = [40, 30, 15, 10, 5]

fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
ax1.axis('equal')
plt.title("Distribution of Technology Devices Used in the USA, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/206.png')
plt.clf()