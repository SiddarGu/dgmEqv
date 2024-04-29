
import matplotlib.pyplot as plt
import numpy as np

# set data
country = ['USA', 'UK', 'Germany', 'France']
renew_energy = [35,50,60,40]
pollution = [2500,2300,2100,2000]

# create figure and plot
fig, ax = plt.subplots(figsize=(15,10))
plt.title('Percentage of Renewable Energy and Pollution in Four Countries in 2021')

x = np.arange(len(country)) 
width = 0.35 
ax.bar(x - width/2, renew_energy, width, label='Renewable Energy(%)', color = 'b')
ax.bar(x + width/2, pollution, width, label='Pollution(Tonnes)', color = 'r')

ax.set_xticks(x)
ax.set_xticklabels(country)
ax.legend()

for i, v in enumerate(renew_energy):
    ax.text(x[i] - width/2, v + 5, str(v), color='b', fontsize=10)
for i, v in enumerate(pollution):
    ax.text(x[i] + width/2, v + 5, str(v), color='r', fontsize=10)

plt.tight_layout()
plt.savefig('Bar Chart/png/438.png')
plt.clf()