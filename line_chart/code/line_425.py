
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 8)) 
ax = fig.add_subplot(111) 
ax.plot(np.arange(2001, 2006), [20, 25, 30, 35, 40], linewidth=2, color='r', marker='o', label="Donation Amount (million dollars)") 
ax.plot(np.arange(2001, 2006), [100, 200, 300, 400, 500], linewidth=2, color='g', marker='o', label="Number of Donors") 
ax.set_title('Donation trends in charitable organizations from 2001 to 2005') 
ax.set_xticks(np.arange(2001, 2006))
ax.set_xlabel('Year') 
ax.set_ylabel('Donation Amount/Number of Donors') 
ax.legend(loc='best', fontsize=8, ncol=1, frameon=True, fancybox=True, shadow=True, borderpad=1, labelspacing=1.2) 
plt.tight_layout() 
plt.savefig('line chart/png/540.png') 
plt.close()