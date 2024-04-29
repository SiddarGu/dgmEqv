
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111)

years = np.array([2010,2011,2012,2013,2014,2015,2016])
solar_energy = np.array([200,300,400,450,500,550,600])
wind_energy = np.array([400,500,600,700,800,900,1000])
hydroelectric_energy = np.array([500,600,800,900,1000,1100,1200])

ax.plot(years,solar_energy,color='green',label='Solar Energy')
ax.plot(years,wind_energy,color='blue',label='Wind Energy')
ax.plot(years,hydroelectric_energy,color='red',label='Hydroelectric Energy')
ax.grid(True)

for a,b in zip(years,solar_energy):
    ax.annotate(str(b),xy=(a,b),xytext=(a-1,b+5))
for a,b in zip(years,wind_energy):
    ax.annotate(str(b),xy=(a,b),xytext=(a-1,b+5))
for a,b in zip(years,hydroelectric_energy):
    ax.annotate(str(b),xy=(a,b),xytext=(a-1,b+5))

plt.title('Renewable Energy Production in the United States from 2010 to 2016',fontsize=20)
plt.xticks(years,rotation=45)
plt.xlabel('Year',fontsize=16)
plt.ylabel('Energy(megawatts)',fontsize=16)
plt.legend(loc='upper left')
plt.tight_layout()

plt.savefig('line chart/png/348.png')
plt.clf()