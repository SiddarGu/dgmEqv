
import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([2018, 2019, 2020, 2021]) 
y1 = np.array([1000, 1200, 800, 1400]) 
y2 = np.array([200, 400, 300, 500]) 
y3 = np.array([800, 800, 500, 900]) 

fig = plt.figure(figsize=(10, 7)) 
ax = fig.add_subplot(111) 
ax.plot(x, y1, label = 'Cost of Goods Sold', marker='o', color='blue') 
ax.plot(x, y2, label = 'Operating Costs', marker='o', color='red') 
ax.plot(x, y3, label = 'Gross Profit', marker='o', color='green') 

for i in range(len(x)): 
    ax.annotate(str(y1[i]), xy=(x[i], y1[i]), 
                xytext=(x[i]-0.25, y1[i]+50)) 
    ax.annotate(str(y2[i]), xy=(x[i], y2[i]), 
                xytext=(x[i]-0.25, y2[i]+50)) 
    ax.annotate(str(y3[i]), xy=(x[i], y3[i]), 
                xytext=(x[i]-0.25, y3[i]+50))

ax.set_xlabel('Year') 
ax.set_ylabel('Million Dollars') 
ax.set_xticks(x) 
ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.0)) 
plt.title('Profit and Loss of a Business in the Year 2018-2021', fontsize=15)
plt.tight_layout() 
plt.savefig('line chart/png/419.png') 
plt.clf()