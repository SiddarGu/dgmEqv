
import matplotlib.pyplot as plt
import numpy as np

State=['California','Texas','New York','Florida']
Charities=[150,200,250,180]
Donations=[100,120,110,90]

fig=plt.figure(figsize=(10,6))
ax = plt.subplot()
width=0.3
x=np.arange(len(State))
ax.bar(x-width/2, Charities, width, label='Charities')
ax.bar(x+width/2, Donations, width, label='Donations(million)')
ax.set_title('Number of charities and donations in four states in 2021')
ax.set_xlabel('State')
ax.set_ylabel('Number')
ax.set_xticks(x)
ax.set_xticklabels(State,rotation=45)
plt.legend(bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig('bar chart/png/538.png')
plt.clf()