
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 8)
y1 = [500,550,600,650,700,750,800]
y2 = [100,150,200,250,300,350,400]

plt.figure(figsize=(8,5))
plt.plot(x, y1, marker='o', markersize=7, color='red', label='Electricity Consumption (kWh)')
plt.plot(x, y2, marker='o', markersize=7, color='blue', label='Solar Energy Generated (kWh)')
plt.title('Change in electricity consumption and solar energy generated in a rural community from January to July 2021')
plt.xticks(x, ('01', '02', '03', '04', '05', '06', '07'))
plt.xlabel('Month')
plt.ylabel('kWh')
plt.legend(loc='lower right')

for a,b,c in zip(x,y1,y2):
    plt.annotate('{}, {}'.format(b,c), xy=(a,b+20), xytext=(a,b+20), rotation='vertical', wrap=True)

plt.tight_layout()
plt.savefig('line chart/png/179.png')
plt.clf()