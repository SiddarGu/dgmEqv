
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Change in court verdict rates from 2015 to 2019') 

ax.plot([2015, 2016, 2017, 2018, 2019], [50, 45, 40, 45, 35], label='Rate of Conviction') 
ax.plot([2015, 2016, 2017, 2018, 2019], [30, 35, 35, 32, 40], label='Rate of Acquittal') 
ax.plot([2015, 2016, 2017, 2018, 2019], [20, 20, 25, 23, 25], label='Rate of Dismissal') 
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.03))
ax.set_xticks([2015, 2016, 2017, 2018, 2019])
plt.tight_layout()
plt.savefig('line chart/png/442.png')
plt.clf()