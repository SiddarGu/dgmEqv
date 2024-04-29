
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(12,8)) 
ax = fig.add_subplot(111) 
ax.bar(['North America', 'Europe', 'Asia', 'South America'], [25, 30, 20, 45], bottom=0, label='Laws') 
ax.bar(['North America', 'Europe', 'Asia', 'South America'], [100, 110, 90, 120], bottom=25, label='Regulations') 
plt.xticks(rotation=45, ha="right") 
plt.yticks(range(0, 160, 10)) 
ax.set_title('Number of laws and regulations in four regions of the world in 2021') 
plt.legend() 
plt.tight_layout() 
plt.savefig('bar chart/png/33.png') 
plt.clf()