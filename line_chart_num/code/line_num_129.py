

import matplotlib.pyplot as plt

Month = ["January","February","March","April","May","June"] 
Users_A = [1000,1100,1200,1400,1500,1600] 
Users_B = [1200,1300,1400,1500,1600,1700] 
Users_C = [1500,1350,1450,1550,1700,1800]

plt.figure(figsize=(10,8))

ax = plt.subplot()
ax.plot(Month,Users_A,label='Users A(millions)',marker='o')
ax.plot(Month,Users_B,label='Users B(millions)',marker='s')
ax.plot(Month,Users_C,label='Users C(millions)',marker='^')

ax.set_title('Growth in Social Media Users from January to June, 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Number of users')

ax.set_xticks(Month)
plt.legend(loc='best')

for x,y in zip(Month,Users_A):
    ax.annotate(str(y),xy=(x,y))
for x,y in zip(Month,Users_B):
    ax.annotate(str(y),xy=(x,y))
for x,y in zip(Month,Users_C):
    ax.annotate(str(y),xy=(x,y))

plt.tight_layout()
plt.savefig('line chart/png/322.png')
plt.clf()