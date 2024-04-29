
import matplotlib.pyplot as plt
import numpy as np

year = np.array([2001, 2002, 2003, 2004])
Criminal_Cases = np.array([400, 450, 500, 550])
Civil_Cases = np.array([450, 500, 550, 600])
Traffic_Cases = np.array([220, 210, 230, 250])

fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(111)
ax1.plot(year, Criminal_Cases, marker='o',label='Criminal Cases', color='green')
ax1.plot(year, Civil_Cases, marker='o',label='Civil Cases', color='blue')
ax1.plot(year, Traffic_Cases, marker='o',label='Traffic Cases', color='red')
ax1.set_title('Cases filed in the court of law between 2001 and 2004')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number')
plt.xticks(year)
ax1.legend(loc='upper left')
plt.tight_layout()

for a,b in zip(year, Criminal_Cases): 
    ax1.annotate(str(b),xy=(a,b))
for a,b in zip(year, Civil_Cases):
    ax1.annotate(str(b),xy=(a,b))
for a,b in zip(year, Traffic_Cases):
    ax1.annotate(str(b),xy=(a,b))

plt.savefig('line chart/png/90.png')
plt.clf()