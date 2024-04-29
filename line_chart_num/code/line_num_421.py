
import matplotlib.pyplot as plt

#set the figure
plt.figure(figsize=(16,8))

#get data
month = ['January','February','March','April','May','June','July','August','September','October','November','December']
solar = [200,250,280,320,400,450,500,480,450,420,380,350]
wind = [300,350,330,370,450,500,550,520,500,470,430,400]
hydro = [400,450,420,480,500,550,600,580,550,520,480,450]

#plot line chart
plt.plot(month,solar, color='#e0e1e2', linestyle='-', marker='o', label='Solar Energy(KWh)')
plt.plot(month,wind, color='#27496d', linestyle='-', marker='o', label='Wind Energy(KWh)')
plt.plot(month,hydro, color='#a1d1e6', linestyle='-', marker='o', label='Hydro Energy(KWh)')

#set xticks
plt.xticks(month, rotation=45)

#label each point
for a, b, c in zip(month, solar, wind):
    plt.annotate(str(b)+','+str(c),xy=(a,b+c), xytext=(-4,4),textcoords='offset points')

#set legend
plt.legend(loc='best')

#set title
plt.title('Renewable Energy Production in a Year in a Mountainous Region')

#tight layout
plt.tight_layout()

#save figure
plt.savefig('line chart/png/437.png')

#clear figure
plt.clf()