

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))
plt.grid(True, color='#95a5a6', linestyle='--', linewidth=1,alpha=0.3)

month = ['January','February','March','April','May','June','July','August']
revenue = [2000,2200,2500,1800,1900,1700,2300,2100]
orders = [100,150,180,140,130,120,160,150]
average_cost = [20,19,18,21,20,22,20,19]

plt.plot(month,revenue,'r-',label='Revenue')
plt.plot(month,orders,'g-',label='Orders')
plt.plot(month,average_cost,'b-',label='Average Cost')

plt.xlabel('Month',fontsize=14)
plt.ylabel('Revenue,Orders,Average Cost',fontsize=14)
plt.title('Revenue, Orders and Average Cost of Fast-Food Franchise in 2020',fontsize=16)

plt.xticks(month,rotation=45,fontsize=12)

plt.legend(loc='upper left',bbox_to_anchor=(0.1,1.01),markerscale=3,borderaxespad=0,fontsize=14)

plt.tight_layout()

plt.savefig('line chart/png/111.png')

plt.clf()