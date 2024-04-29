
import matplotlib.pyplot as plt 
import numpy as np 

plt.figure(figsize=(10,8)) 
ax = plt.subplot() 

data = np.array([[2004, 65, 400, 200], 
                 [2008, 72, 420, 220], 
                 [2012, 60, 440, 240],
                 [2016, 69, 460, 260],
                 [2020, 64, 480, 280]])

ax.plot(data[:,0], data[:,1], label="Voting Turnout(%)")
ax.plot(data[:,0], data[:,2], label="Spending on Healthcare(billion dollars)")
ax.plot(data[:,0], data[:,3], label="Spending on Education(billion dollars)")

ax.set_title("Voter Turnout and Government Spending in the United States from 2004 to 2020")
ax.set_xlabel("Year")
ax.set_ylabel("Amount")
ax.legend(loc="upper left", fontsize="medium", frameon=True, shadow=True, bbox_to_anchor=(1, 1))

plt.xticks(data[:,0])
plt.tight_layout()

plt.savefig('line chart/png/156.png') 
plt.clf()