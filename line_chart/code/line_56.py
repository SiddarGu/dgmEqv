
import matplotlib.pyplot as plt 
import numpy as np

data = [[2016,20,10],
        [2017,22,12],
        [2018,25,14],
        [2019,27,16],
        [2020,29,18]]
 
fig = plt.figure(figsize=(12,6)) 
ax = fig.add_subplot(111) 
ax.set_title('Increase in Football Stadium Attendance and Revenue from 2016 to 2020') 
ax.set_xlabel('Year') 
ax.set_ylabel('Attendance (million people) and Revenue (billion dollars)')
ax.plot(np.array(data)[:,0], np.array(data)[:,1], label='Attendance (million people)')
ax.plot(np.array(data)[:,0], np.array(data)[:,2], label='Revenue (billion dollars)')
ax.legend(loc='best')
plt.xticks(np.array(data)[:,0], rotation=30)
plt.tight_layout()
plt.savefig('line chart/png/251.png')
plt.clf()