
import matplotlib.pyplot as plt

x = [2010,2011,2012,2013,2014]
y1 = [250,280,320,350,380]
y2 = [300,340,380,420,460]
y3 = [400,450,500,550,600]
y4 = [450,500,550,600,650]

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label = 'Solar energy(MW)')
plt.plot(x, y2, label = 'Wind energy(MW)')
plt.plot(x, y3, label = 'Nuclear energy(MW)')
plt.plot(x, y4, label = 'Hydroelectric energy(MW)')
plt.title("Energy Production from Renewable Sources in the United States")
plt.xlabel('Year')
plt.ylabel('Energy Production(MW)')
plt.xticks(x)
plt.legend(loc = 'lower right',bbox_to_anchor=(1.3, 0.5), fontsize = 'x-large')
plt.tight_layout()
plt.savefig("line chart/png/386.png")
plt.clf()