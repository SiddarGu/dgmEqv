
import matplotlib.pyplot as plt 
import numpy as np 

data = [[1,40,7,1000], [2,45,8,1200], [3,35,9,1400], [4,38,8,1100], [5,37,9,1500]] 

fig, ax = plt.subplots(figsize=(10,6)) 
ax.set_xlabel('Week', fontsize=14)
ax.set_ylabel('Average Hours Worked, Average Productivity, Average Salary', fontsize=14)
ax.set_title('Work Performance of Employees in 2021', fontsize=16)
ax.grid(axis='y', color='lightgray', linestyle='--', linewidth=1)

w = np.array(data)[:,0]
h = np.array(data)[:,1]
p = np.array(data)[:,2]
s = np.array(data)[:,3]

ax.plot(w,h, color='blue', label='Average Hours Worked')
ax.plot(w,p, color='green', label='Average Productivity')
ax.plot(w,s, color='red', label='Average Salary')
ax.legend(loc='best', fontsize=14)

for i, txt in enumerate(h):
    ax.annotate(txt, (w[i],h[i]), fontsize=14)
for i, txt in enumerate(p):
    ax.annotate(txt, (w[i],p[i]), fontsize=14)
for i, txt in enumerate(s):
    ax.annotate(txt, (w[i],s[i]), fontsize=14)

ax.set_xticks(w)
plt.tight_layout()
plt.savefig(r'line chart/png/180.png')
plt.clf()