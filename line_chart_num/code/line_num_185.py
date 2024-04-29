
import matplotlib.pyplot as plt
import numpy as np

# prepare data
year = np.array([2011,2012,2013,2014,2015])
enrollment_rate = np.array([90,88,85,80,83])
graduation_rate = np.array([70,75,72,77,79])
attrition_rate = np.array([20,15,22,18,16])

# figure
fig = plt.figure(figsize=(15,8))

# add subplot
ax1 = fig.add_subplot(111)

# plot and annotate
ax1.plot(year,enrollment_rate,label='enrollment rate')
for a,b in zip(year,enrollment_rate):
    ax1.annotate('%.1f'%b,xy=(a,b),xytext=(0,2),textcoords='offset points',rotation=45)

ax1.plot(year,graduation_rate,label='graduation rate')
for a,b in zip(year,graduation_rate):
    ax1.annotate('%.1f'%b,xy=(a,b),xytext=(0,2),textcoords='offset points',rotation=45)

ax1.plot(year,attrition_rate,label='attrition rate')
for a,b in zip(year,attrition_rate):
    ax1.annotate('%.1f'%b,xy=(a,b),xytext=(0,2),textcoords='offset points',rotation=45)

# xticks
plt.xticks(year)

# legend
plt.legend(loc=2, bbox_to_anchor=(1,1.03))

# title
plt.title('Changes in Enrollment, Graduation and Attrition Rates of University Students from 2011 to 2015')

# save
plt.tight_layout()
plt.savefig('line chart/png/6.png')

# clear current image
plt.clf()