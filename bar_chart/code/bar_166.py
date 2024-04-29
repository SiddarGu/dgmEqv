
import matplotlib.pyplot as plt
import numpy as np

Type_of_Arts = np.array(['Music','Theater','Visual Arts','Dance'])
Number_of_Events = np.array([50,60,80,40])
Number_of_Artists = np.array([200,150,250,100])

fig, ax = plt.subplots(figsize=(10, 5))
plt.bar(Type_of_Arts, Number_of_Events, label='Number of Events', width=0.4, bottom=Number_of_Artists)
plt.bar(Type_of_Arts, Number_of_Artists, label='Number of Artists', width=0.4)

ax.set_xticks(Type_of_Arts)
ax.set_xticklabels(Type_of_Arts, rotation=90, wrap=True)
plt.title('Number of Arts Events and Artists in 2021')
plt.legend()
plt.tight_layout()

plt.savefig('bar chart/png/357.png')
plt.clf()