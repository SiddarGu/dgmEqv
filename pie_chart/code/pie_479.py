
import matplotlib.pyplot as plt
pie_data = [20,30,40,10]
labels = ["Rail","Air","Road","Water"]
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.pie(pie_data, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90,textprops={'fontsize': 14})
ax.axis('equal')
ax.set_title("Distribution of Transportation Modes in the USA, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/241.png')
plt.clf()