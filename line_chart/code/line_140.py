
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(10,8))
ax1=fig.add_subplot(111)

year=[2000,2001,2002,2003,2004]
crop_A=[200,220,240,260,280]
crop_B=[100,105,110,115,120]
crop_C=[150,160,170,180,190]
crop_D=[250,265,280,295,310]

ax1.plot(year,crop_A,c='b',marker='o',label='Crop A')
ax1.plot(year,crop_B,c='r',marker='x',label='Crop B')
ax1.plot(year,crop_C,c='g',marker='*',label='Crop C')
ax1.plot(year,crop_D,c='y',marker='s',label='Crop D')

ax1.set_title('Crop Production in four regions in 2000-2004')
ax1.set_xlabel('Year')
ax1.set_ylabel('Tonnes')
ax1.set_xticks(np.arange(min(year), max(year)+1, 1.0))
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/486.png')
plt.clf()