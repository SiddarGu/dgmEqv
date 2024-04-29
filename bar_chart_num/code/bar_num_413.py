
import matplotlib.pyplot as plt 
import numpy as np 

data = np.array([[50,80,450],[70,90,500],[60,70,400],[80,100,470]])
x_labels = ['USA','UK','Germany','France']
category = ['Hotels','Restaurants','Tourists']

fig, ax = plt.subplots(figsize=(10, 6))
bottom = np.zeros(len(x_labels))
for i,cat in enumerate(category):
    ax.bar(x_labels,data[:,i],bottom=bottom, label=cat, width=0.5)
    bottom += data[:,i]
plt.title('Number of hotels, restaurants and tourists in four countries in 2021')
plt.xticks(x_labels)
plt.legend()

for x,y in zip(x_labels,data.sum(axis=1)):
    plt.text(x,y,y, ha='center', va='bottom')

plt.tight_layout()
plt.savefig("Bar Chart/png/283.png")
plt.show()
plt.clf()