
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

sources = ['Renewable','Coal','Natural Gas','Nuclear','Oil']
percentage = [42,25,18,10,5]

ax.pie(percentage, labels=sources, textprops={'fontsize': 14, 'color':'black'}, autopct='%1.1f%%',
        labeldistance=1.2, rotatelabels=True)
ax.axis('equal')
ax.set_title('Distribution of Energy Sources in the USA, 2023', fontsize=14)

plt.tight_layout()
plt.savefig('pie chart/png/407.png')
plt.clf()