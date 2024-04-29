
import matplotlib.pyplot as plt
import numpy as np

Month = ['January', 'February', 'March', 'April']
ManufacturingA = [10,9,11,8]
ManufacturingB = [12,13,14,15]
ManufacturingC = [8,11,12,14]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
ax.bar(Month,ManufacturingA,label='Manufacturing A',bottom=0,width=0.2,align='center')
ax.bar(Month,ManufacturingB,label='Manufacturing B',bottom=ManufacturingA,width=0.2,align='center')
ax.bar(Month,ManufacturingC,label='Manufacturing C',bottom=[sum(x) for x in zip(ManufacturingA,ManufacturingB)],width=0.2,align='center')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),fancybox=True, shadow=True, ncol=5)
plt.title('Manufacturing output in three categories from January to April 2021')
plt.xticks(Month)
plt.tight_layout()
plt.savefig('bar chart/png/266.png')
plt.clf()