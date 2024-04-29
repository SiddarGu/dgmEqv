
import matplotlib.pyplot as plt 

plt.figure(figsize=(10,8))

ax = plt.subplot(111)

x=[2020,2021,2022,2023,2024]
y1=[7.79,7.88,7.97,8.07,8.16]
y2=[17.8,18.2,18.5,18.9,19.4]

ax.plot(x,y1,color='skyblue',marker='o',label='Population(million)')
ax.plot(x,y2,color='orange',marker='o',label='Birth Rate')

ax.set_xticks(x)
ax.set_xlabel('Year')
ax.set_title('Global Population and Birth Rate from 2020 to 2024')

ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))

plt.tight_layout()
plt.savefig('line chart/png/124.png')
plt.clf()