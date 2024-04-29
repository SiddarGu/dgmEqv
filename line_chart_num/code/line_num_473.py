

import matplotlib.pyplot as plt
import numpy as np

month=['January','February','March','April','May','June','July','August','September','October']
crop_a=[100,110,130,150,200,230,250,230,210,180]
crop_b=[120,130,140,130,150,170,190,180,150,140]
crop_c=[90,95,100,110,120,140,160,130,120,100]

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(1,1,1)
ax.plot(month,crop_a,label='Crop A',color='red',marker='o')
ax.plot(month,crop_b,label='Crop B',color='blue',marker='x')
ax.plot(month,crop_c,label='Crop C',color='green',marker='s')

ax.set_title('Crop Production in a Midwestern State in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Crop Production(tons)')
ax.legend(loc='upper left')
ax.grid(True,linestyle='--',color='gray',alpha=0.5)

for x, y in zip(month, crop_a):
    ax.annotate(y, xy=(x, y), xytext=(-2, 5), textcoords='offset points',rotation=45)
    
for x, y in zip(month, crop_b):
    ax.annotate(y, xy=(x, y), xytext=(-2, 5), textcoords='offset points',rotation=45)
    
for x, y in zip(month, crop_c):
    ax.annotate(y, xy=(x, y), xytext=(-2, 5), textcoords='offset points',rotation=45)

ax.set_xticks(month)
plt.tight_layout()
plt.savefig('line chart/png/466.png')
plt.clf()