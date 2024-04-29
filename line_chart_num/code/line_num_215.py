
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6))
data = np.array([[2010,1000,400,600],[2011,1200,500,700],[2012,1400,550,850],[2013,1600,600,1000],[2014,1800,650,1150]])
x = data[:, 0]
filed = data[:, 1]
resolved = data[:, 2]
pending = data[:, 3]
plt.plot(x, filed, label = 'Cases Filed')
plt.plot(x, resolved, label = 'Cases Resolved')
plt.plot(x, pending, label = 'Cases Pending')
plt.xticks(x)
plt.title('Number of cases in a legal firm from 2010 to 2014')
plt.xlabel('Year')
plt.ylabel('Number of cases')
plt.legend()
for i, txt in enumerate(filed):
    plt.annotate(txt, (x[i],filed[i]))
for i, txt in enumerate(resolved):
    plt.annotate(txt, (x[i],resolved[i]))
for i, txt in enumerate(pending):
    plt.annotate(txt, (x[i],pending[i]))
plt.tight_layout()
plt.savefig('line chart/png/332.png')
plt.clf()