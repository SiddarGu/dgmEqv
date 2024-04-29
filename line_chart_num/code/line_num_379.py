
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
ax = plt.subplot()
ax.plot([300,400,500,600,700],[0.1,1.2,2.4,3.6,4.8],color='blue',linewidth=2,label='Viscosity Changes')
ax.set_xlabel('Temperature(Kelvin)', fontsize=14)
ax.set_ylabel('Viscosity(cP)', fontsize=14)
ax.set_title('Viscosity Changes of a Gas with Temperature and Pressure Increase', fontsize=18)
ax.set_xticks([300,400,500,600,700]) 
ax.legend(loc='upper left')

for a,b in zip([300,400,500,600,700],[0.1,1.2,2.4,3.6,4.8]): 
    ax.annotate('(%s, %s)' %(a,b), xy=(a,b), xytext=(a - 20, b + 0.2))
plt.tight_layout()
plt.savefig('line chart/png/133.png')
plt.clf()