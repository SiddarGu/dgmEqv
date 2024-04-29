
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 450, 7000, 10000],
        ['UK', 500, 6500, 11000], 
        ['Germany', 400, 6000, 9000], 
        ['France', 470, 7200, 12000]] 

x = np.arange(len(data))
width = 0.2

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

ax.bar(x, [i[1] for i in data], width, label='Hospitals')
ax.bar(x + width, [i[2] for i in data], width, label='Doctors')
ax.bar(x + (2 * width), [i[3] for i in data], width, label='Nurses')

ax.set_xticks(x + (width/2))
ax.set_xticklabels([i[0] for i in data], rotation=90, wrap=True)
ax.legend()

ax.set_title("Number of healthcare facilities, doctors, and nurses in four countries in 2021")

plt.tight_layout()
plt.savefig('bar chart/png/547.png')
plt.clf()