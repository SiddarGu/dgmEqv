
import matplotlib.pyplot as plt 
import numpy as np

plt.figure(figsize=(10,6)) 
ax = plt.subplot(111) 
Country = ["USA", "UK", "Germany", "France"] 
Cases = [50000, 55000, 48000, 52000] 
Settlements = [40000, 45000, 42000, 47000]

bar_width = 0.3
index = np.arange(len(Country))
rects1 = ax.bar(index, Cases, bar_width, color='b', label='Cases')
rects2 = ax.bar(index+bar_width, Settlements, bar_width, color='g', label='Settlements')

ax.set_xlabel('Country') 
ax.set_ylabel('Number of Legal Cases') 
ax.set_title('Number of legal cases and settlements in four countries in 2021') 
ax.set_xticks(index+bar_width/2) 
ax.set_xticklabels(Country, rotation=30, ha="right") 
ax.legend(loc="upper left")

plt.tight_layout() 
plt.savefig("bar chart/png/461.png") 
plt.clf()