
import matplotlib.pyplot as plt 
import numpy as np 

data = np.array([[1000,500],[950,550],[1050,650],[900,700]])
Month=["January","February","March","April"]
x = np.arange(len(Month))

fig, ax = plt.subplots(figsize=(8,6))
ax.bar(x,data[:,0],width=0.4,label="Full Time Employees")
ax.bar(x+0.4,data[:,1],width=0.4,label="Part Time Employees")
ax.set_xticks(x+0.2)
ax.set_xticklabels(Month)
ax.set_title("Number of full-time and part-time employees from January to April 2021")
ax.legend()
plt.tight_layout()

for i in range(len(x)):
    ax.annotate(data[i,0],(x[i]-0.2,data[i,0]+20))
    ax.annotate(data[i,1],(x[i]+0.6,data[i,1]+20))

plt.savefig("Bar Chart/png/466.png")
plt.clf()