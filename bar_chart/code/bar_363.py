
import matplotlib.pyplot as plt 
import numpy as np
Country = ['USA', 'UK', 'Germany', 'France'] 
Production_A = np.array([1000, 900, 1100, 800]) 
Production_B = np.array([1200, 1300, 1400, 1500]) 
Production_C = np.array([800, 1100, 1200, 1400]) 

x = np.arange(len(Country)) 
fig, ax = plt.subplots(figsize=(8, 6)) 
width = 0.25 
ax.bar(x - width, Production_A, width, label='Production A(million)') 
ax.bar(x, Production_B, width, label='Production B(million)') 
ax.bar(x + width, Production_C, width, label='Production C(million)') 
ax.set_title('Manufacturing and Production output in four countries in 2021') 
ax.set_xticks(x) 
ax.set_xticklabels(Country, rotation=45) 
ax.legend(loc='best') 
plt.tight_layout() 
plt.savefig('bar chart/png/90.png') 
plt.clf()