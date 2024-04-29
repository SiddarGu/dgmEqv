
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 450, 300], 
        ['UK', 300, 250], 
        ['Germany', 240, 210], 
        ['France', 180, 150]]

X = np.arange(len(data))
width = 0.25

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()
ax.bar(X - width, [i[1] for i in data], width=width, label='Internet Users(million)')
ax.bar(X, [i[2] for i in data], width=width, label='Smartphones(million)')
ax.set_xticks(X)
ax.set_xticklabels([i[0] for i in data], rotation=45, ha='right', wrap=True)
ax.set_title('Number of internet users and smartphones in four countries in 2021')
ax.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.savefig('bar chart/png/139.png')
plt.clf()