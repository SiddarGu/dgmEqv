
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[4000, 4], 
                 [3000, 24], 
                 [2000, 12]]) 
  
Mode = ['Air', 'Sea', 'Rail'] 
  
cost = data[:, 0] 
time = data[:, 1] 
  
x = np.arange(len(Mode)) 
  
plt.figure(figsize=(10,7))
ax = plt.subplot() 
ax.bar(x, cost, width = 0.5,
       color ='b', label ='Cost') 
ax.bar(x, time, width = 0.5, 
       bottom = cost, color ='g', 
       label ='Time') 
  
ax.set_ylabel('(USD, hour)') 
ax.set_title('Cost and time of transportation using air, sea and rail in 2021') 
ax.set_xticks(x) 
ax.set_xticklabels(Mode) 
ax.legend(loc='upper right') 

# add labels
for i, v in enumerate(data.T.flatten()):
    ax.text(x[i%3], v+0.5, str(v), color='black', fontweight='bold',
            ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/282.png')
plt.clf()