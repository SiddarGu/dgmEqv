
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

country = ['USA','UK','Germany','France']
education = [70,60,50,40]
health = [90,80,70,60]
infrastr = [120,100,90,80]

x = np.arange(len(country)) 
width = 0.25 
plt.bar(x, education, width, label='Education', bottom=0)
plt.bar(x, health, width, label='Health', bottom=education)
plt.bar(x, infrastr, width, label='Infrastructure', bottom=np.array(education)+np.array(health))

plt.xticks(x, country)
plt.xlabel("Country")
plt.ylabel("Expenditure (billion)")
plt.title("Government expenditure on education, health and infrastructure in four countries in 2021")
plt.legend(loc='upper left')

ax.annotate('{}'.format(education[0]), xy=(x[0], education[0]/2), ha='center', va='center')
ax.annotate('{}'.format(health[0]), xy=(x[0], education[0] + health[0]/2), ha='center', va='center')
ax.annotate('{}'.format(infrastr[0]), xy=(x[0], education[0] + health[0] + infrastr[0]/2), ha='center', va='center')
ax.annotate('{}'.format(education[1]), xy=(x[1], education[1]/2), ha='center', va='center')
ax.annotate('{}'.format(health[1]), xy=(x[1], education[1] + health[1]/2), ha='center', va='center')
ax.annotate('{}'.format(infrastr[1]), xy=(x[1], education[1] + health[1] + infrastr[1]/2), ha='center', va='center')
ax.annotate('{}'.format(education[2]), xy=(x[2], education[2]/2), ha='center', va='center')
ax.annotate('{}'.format(health[2]), xy=(x[2], education[2] + health[2]/2), ha='center', va='center')
ax.annotate('{}'.format(infrastr[2]), xy=(x[2], education[2] + health[2] + infrastr[2]/2), ha='center', va='center')
ax.annotate('{}'.format(education[3]), xy=(x[3], education[3]/2), ha='center', va='center')
ax.annotate('{}'.format(health[3]), xy=(x[3], education[3] + health[3]/2), ha='center', va='center')
ax.annotate('{}'.format(infrastr[3]), xy=(x[3], education[3] + health[3] + infrastr[3]/2), ha='center', va='center')
plt.tight_layout()
plt.savefig('Bar Chart/png/112.png')
plt.clf()