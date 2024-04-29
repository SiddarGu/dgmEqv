
import matplotlib.pyplot as plt
import numpy as np

Country=['USA','UK','Germany','France']
Cases_Opened=[500,450,360,400]
Cases_Closed=[400,350,320,380]

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
ax.bar(Country,Cases_Opened,width=0.4,label='Cases Opened')
ax.bar(Country,Cases_Closed,width=0.4,bottom=Cases_Opened,label='Cases Closed')
ax.set_title('Number of legal cases opened and closed in four countries in 2021')
ax.legend(loc='best')
plt.xticks(Country,rotation=45)
plt.tight_layout()
plt.savefig('bar chart/png/462.png')
plt.clf()