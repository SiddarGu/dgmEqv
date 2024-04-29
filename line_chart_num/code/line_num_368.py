
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize']=(20,10)

x = ['January','February','March','April','May','June','July','August']
y1 = [1000,1100,1300,1500,1300,1100,1000,900]
y2 = [800,900,1000,1200,1400,1600,1800,2000]
y3 = [1200,1400,1500,1300,1100,1000,900,800]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(x,y1,label='Wind Energy Generation(kWh)',marker='o')
ax1.plot(x,y2,label='Solar Energy Generation(kWh)',marker='o')
ax1.plot(x,y3,label='Hydro Energy Generation(kWh)',marker='o')
ax1.legend(loc='upper center')
ax1.set_title('Renewable Energy Production in New York in 2021',fontsize=20)
ax1.grid(True)
ax1.set_xticks(np.arange(len(x)))
ax1.set_xticklabels(x, fontsize=15,rotation=30,ha='right',wrap=True)

for i,j in zip(x,y1):
    ax1.annotate(str(j),xy=(i,j),fontsize=20)
for i,j in zip(x,y2):
    ax1.annotate(str(j),xy=(i,j),fontsize=20)
for i,j in zip(x,y3):
    ax1.annotate(str(j),xy=(i,j),fontsize=20)

fig.tight_layout()
plt.savefig(r'line chart/png/139.png')
plt.clf()