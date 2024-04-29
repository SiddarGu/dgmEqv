

import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 400, 800, 900], ['UK', 550, 1000, 1100], ['Germany', 500, 850, 1000], ['France', 650, 950, 1200]] 

#Define the parameters for the figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
width = 0.2

#Plot the data
ax.bar(np.arange(len(data))-width, [i[1] for i in data], width, label = 'Theatre Performances')
ax.bar(np.arange(len(data)), [i[2] for i in data], width, label = 'Museums Visitors')
ax.bar(np.arange(len(data))+width, [i[3] for i in data], width, label = 'Art Galleries Visitors')

#Set the axes
ax.set_xlabel('Country')
ax.set_ylabel('Number of Visitors')
ax.set_title('Number of theatre performances and visitors to museums and art galleries in four countries in 2021')
ax.set_xticks(np.arange(len(data)))
ax.set_xticklabels([i[0] for i in data], rotation = 30, wrap = True)
ax.legend(loc='best')

fig.tight_layout()

#Save the figure
plt.savefig('bar chart/png/44.png')

#Clear the image state
plt.clf()