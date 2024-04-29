
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Donations = [30, 20, 25, 15]
Volunteers = [100000, 90000, 80000, 70000]

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(Country, Donations, label="Donations (million)")
ax.bar(Country, Volunteers, bottom=Donations, label="Number of Volunteers")

for i in range(len(Donations)):
    ax.annotate(Donations[i], xy=(i-0.2, Donations[i]/2))
    ax.annotate(Volunteers[i], xy=(i-0.2, Donations[i]+Volunteers[i]/2))

plt.xticks(np.arange(len(Country)), Country)
plt.title('Number of donations and volunteers in four countries in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/123.png')
plt.clf()