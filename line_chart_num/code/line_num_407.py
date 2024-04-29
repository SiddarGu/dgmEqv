
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,8))

Year = np.arange(2001, 2005)
Crime_Rate = [0.08, 0.10, 0.09, 0.12]
Police_Officers = [40000, 42000, 44000, 46000]
Prisons = [40, 43, 45, 47]

plt.plot(Year, Crime_Rate, '--', color='#FFC0CB', label='Crime Rate')
plt.plot(Year, Police_Officers, '-', color='#FFA500', label='Number of Police Officers')
plt.plot(Year, Prisons, '-.', color='#6495ED', label='Number of Prisons')

plt.title('Crime rate and police presence in the United States from 2001 to 2004', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Crime Rate & Number of Police Officers & Number of Prisons', fontsize=12)

plt.xticks(Year, fontsize=10)
plt.yticks(fontsize=10)

plt.legend(loc='upper left', bbox_to_anchor=(0, 1))

for a,b,c in zip(Year,Crime_Rate,Police_Officers):
    plt.text(a,b+0.005,b,ha='center', va= 'bottom',fontsize=12)
    plt.text(a,c+5000,c,ha='center', va= 'bottom',fontsize=12)

for a,b in zip(Year,Prisons):
    plt.text(a,b+2,b,ha='center', va= 'bottom',fontsize=12)

plt.tight_layout()
plt.savefig('line chart/png/601.png')
plt.clf()