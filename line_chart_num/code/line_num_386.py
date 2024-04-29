
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(20,10))
plt.subplot(1,1,1)

Quarter = np.array(['Q1 2020','Q2 2020','Q3 2020','Q4 2020'])
Users_A = np.array([500,600,650,700])
Users_B = np.array([400,450,500,550])
Users_C = np.array([600,700,800,900])

plt.plot(Quarter,Users_A,label='Number of Users A(million)',color='b', linewidth=2.0)
plt.plot(Quarter,Users_B,label='Number of Users B(million)',color='g', linewidth=2.0)
plt.plot(Quarter,Users_C,label='Number of Users C(million)',color='r', linewidth=2.0)

plt.xlabel('Quarter',fontsize=20)
plt.ylabel('Number of Users',fontsize=20)
plt.title('Quarterly Growth of Social Media Users in 2020',fontsize=30)

plt.xticks(Quarter)

plt.legend(fontsize=20,loc='best')

for a,b,c in zip(Quarter,Users_A,Users_B):
    plt.text(a,b,'%.2f'%b,horizontalalignment='center',fontsize=20)
    plt.text(a,c,'%.2f'%c,horizontalalignment='center',fontsize=20)

plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/193.png')

plt.clf()