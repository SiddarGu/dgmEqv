
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)

labels = ["Solar","Wind","Hydroelectricity","Nuclear","Natural Gas"]
sizes = [25,20,30,15,10]
colors = ['lightgreen','lightblue','yellowgreen','red','orange']
explode = (0.2,0,0,0,0)

ax.pie(sizes,labels=labels, colors=colors, autopct='%1.1f%%',explode=explode,startangle=90,shadow=False,pctdistance=0.7,labeldistance=1.1)
ax.axis('equal')
plt.title("Energy Sources for Electricity Generation in the USA, 2023")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('pie chart/png/7.png')
plt.show()
plt.clf()