
import matplotlib.pyplot as plt

Sectors=['Automotive','Aerospace','Industrial Machinery','Electronics','Construction','Chemical','Textiles','Food & Beverage','Other']
Share=[20,10,15,15,20,10,10,5,5]

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111)
ax.pie(Share, labels=Sectors,autopct='%1.1f%%',textprops={'fontsize': 10},startangle=90,radius=1)
ax.set_title('Distribution of Manufacturing Sectors in the USA, 2023',fontsize=20)
plt.tight_layout()
plt.savefig('pie chart/png/231.png')
plt.clf()