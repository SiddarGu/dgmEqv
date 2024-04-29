
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,6))
plt.title('Crop and Livestock Production in Four Major Regions in 2021')
plt.xlabel('Region')
plt.ylabel('Production')

data = np.array([[500,430], [300,450], [400,470], [250,500]])
x_labels = np.array(['North America', 'Europe', 'Asia', 'Africa'])

x = np.arange(len(x_labels))
width = 0.35

plt.bar(x, data[:,0],width, label='Crops', bottom=0)
plt.bar(x, data[:,1],width, label='Livestock', bottom=data[:,0])

plt.xticks(x,x_labels, rotation='vertical')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/405.png')
plt.clf()