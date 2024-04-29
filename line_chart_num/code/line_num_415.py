
import matplotlib.pyplot as plt 
import numpy as np 

plt.figure(figsize=(10,6)) 
x = np.array([1,2,3,4,5,6,7,8,9]) 
y1 = np.array([10000,20000,30000,40000,50000,60000,70000,80000,90000]) 
y2 = np.array([0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]) 

plt.plot(x, y1, marker='o',label="Number of Visitors") 
plt.plot(x, y2, marker='o',label="Average Conversion Rate") 
plt.xticks(x,('January','February','March','April','May','June','July','August','September'))

plt.title('Changes in the number of visitors and average conversion rate for an online store in 2021')
plt.legend(loc="best")

for a,b in zip(x, y1):
    plt.text(a,b,b,ha="center",va="bottom",fontsize=10)
for a,b in zip(x, y2):
    plt.text(a,b,b,ha="center",va="bottom",fontsize=10)

plt.tight_layout()
plt.savefig('line chart/png/280.png',format='png')
plt.clf()