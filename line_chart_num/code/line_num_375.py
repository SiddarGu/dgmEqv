

import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(10,7))
plt.plot(np.arange(2017,2022),[20,22,25,28,30],color='red',label='Revenue From Sports Events (billion dollars)',marker='o')
plt.plot(np.arange(2017,2022),[18,19,21,23,24],color='blue',label='Revenue From Entertainment Events (billion dollars)',marker='o')
plt.xticks(np.arange(2017,2022))
plt.title('Comparison of Revenue from Sports and Entertainment Events in the Past 5 Years')
plt.xlabel('Year')
plt.ylabel('Revenue (billion dollars)')
plt.legend(loc='upper left')

for x,y in zip(np.arange(2017,2022),[20,22,25,28,30]):
    plt.annotate(y,xy=(x,y),xytext=(-5,5),textcoords='offset points')
for x,y in zip(np.arange(2017,2022),[18,19,21,23,24]):
    plt.annotate(y,xy=(x,y),xytext=(-5,5),textcoords='offset points')

plt.tight_layout()
plt.savefig('line chart/png/514.png')
plt.close(fig)