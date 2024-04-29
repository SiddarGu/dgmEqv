
import matplotlib.pyplot as plt
import matplotlib

plt.figure(figsize=(10,10))
ax = plt.subplot(111)
destination = ['Europe', 'Asia', 'Americas', 'Africa', 'Australia and Oceania']
percentage = [30, 25, 20, 15, 10]

ax.pie(percentage, labels=destination, autopct='%1.1f%%', startangle=90, pctdistance=0.8, labeldistance=1.1)
ax.axis('equal')
ax.set_title('Global Tourism Distribution in 2023', fontdict={'fontsize': 16, 'fontweight': 'bold'}, pad=20)

plt.xticks(())
plt.tight_layout()
plt.savefig('pie chart/png/475.png')
plt.clf()