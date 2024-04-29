
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[750,1000],[900,1200],[500,800],[600,700]])
Category = ['Clothing', 'Electronics','Grocery', 'Toys']

fig = plt.figure(figsize = (10,8))
ax = fig.add_subplot(1,1,1)

ax.bar(Category, data[:,0], label = 'Online sales(million)',bottom = np.sum(data[:,1:], axis=1))
ax.bar(Category, data[:,1], label = 'Store sales(million)')

for i, v in enumerate(data.flatten()):
    ax.text(i/2+0.2, v+10, str(v), color='black', ha='center', va='bottom')

ax.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1, fontsize = 8)

plt.xticks(np.arange(len(Category)), Category, rotation=0, fontsize = 10)
plt.title('Comparison of online and store sales in four categories in 2021', fontsize = 12)
plt.tight_layout()
plt.savefig('Bar Chart/png/128.png')
plt.clf()