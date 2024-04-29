

import matplotlib.pyplot as plt 
import numpy as np 

data = np.array([[2.5,3.5,1.2],[2.8,4.2,1.3],[3.5,4.9,1.4],[3.2,4.3,1.6],[4.1,5.2,1.7],[4.2,5.4,1.9]]) 

month = ['January','February','March','April','May','June'] 

fig = plt.figure(figsize=(10,6)) 
ax = fig.add_subplot(111) 

ax.plot(month, data[:, 0], label="Online Sales", color='#0099FF', marker='o') 
ax.plot(month, data[:, 1], label="Retail Store Sales", color='#FF9900', marker='o') 
ax.plot(month, data[:, 2], label="Wholesale Sales", color='#33CC33', marker='o') 

ax.set_title("Comparison of Sales between Online, Retail Store and Wholesale in 2020") 
ax.set_xlabel('Month') 
ax.set_ylabel('Sales') 

ax.grid(linestyle='--', linewidth=0.5, alpha=0.2) 
ax.set_xticks(month) 

ax.legend(loc='upper left', bbox_to_anchor=(1,1)) 

plt.tight_layout() 
plt.savefig('line chart/png/178.png') 
plt.clf()