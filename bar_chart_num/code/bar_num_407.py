
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(20,10)) 
ax = fig.add_subplot(111) 
ax.bar(['USA','China','UK','Germany'], [3000,5000,2000,4000], color='green', label='Solar Production (MWh)', bottom=0)
ax.bar(['USA','China','UK','Germany'], [4000,6000,3000,5000], color='blue', label='Wind Production (MWh)', bottom=[3000,5000,2000,4000])
ax.bar(['USA','China','UK','Germany'], [5000,7000,4000,6000], color='orange', label='Hydro Production (MWh)', bottom=[7000,11000,5000,9000])
ax.set_title('Energy production from solar, wind and hydro in four countries in 2021', fontsize=20)
ax.legend(fontsize=15)
ax.set_xlabel('Country', fontsize=15)
ax.set_ylabel('Production (MWh)', fontsize=15)
ax.tick_params(axis='x', labelsize=13)
ax.tick_params(axis='y', labelsize=13)
ax.set_xticks(['USA','China','UK','Germany'])
for i, v in enumerate([3000,5000,2000,4000]):
    ax.text(i-.25, v/2, str(v), color='black', fontsize=13)
for i, v in enumerate([7000,11000,5000,9000]):
    ax.text(i-.25, v/2, str(v), color='black', fontsize=13)
for i, v in enumerate([11000,17000,9000,15000]):
    ax.text(i-.25, v/2, str(v), color='black', fontsize=13)
plt.tight_layout()
plt.savefig('Bar Chart/png/35.png') 
plt.clf()