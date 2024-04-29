
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Research_Papers = [20000,30000,18000,23000]
Patents = [4500,5000,4000,4700]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

ax.bar(Country, Research_Papers, label='Research Papers', bottom=Patents, width=0.6, align='center')
ax.bar(Country, Patents, label='Patents', width=0.6, align='center')

ax.set_xticks(Country)
ax.set_title('Number of research papers and patents in four countries in 2021')
ax.set_xlabel("Country")
ax.set_ylabel("Number")
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/443.png')
plt.show()
plt.clf()