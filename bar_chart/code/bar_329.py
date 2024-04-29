
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 10000, 15000], 
        ['UK', 9000, 14000], 
        ['Germany', 8000, 13000], 
        ['France', 9000, 12000]]

arr_data = np.array(data)

fig = plt.figure(figsize = (10, 5))
ax = fig.add_subplot(111)

width = 0.4
ind = np.arange(arr_data.shape[0])

ax.bar(ind, arr_data[:, 1], width, color = 'green', label = 'Civil Cases')
ax.bar(ind + width, arr_data[:, 2], width, color = 'yellow', label = 'Criminal Cases')
ax.legend(loc = 'best')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(arr_data[:, 0], rotation = 'vertical', wrap = True)
ax.set_title('Number of civil and criminal cases in four countries in 2021')
plt.tight_layout()
plt.savefig('bar chart/png/495.png')
plt.clf()