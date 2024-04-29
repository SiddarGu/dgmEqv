
import matplotlib.pyplot as plt
import numpy as np

data=np.array([[2020, 310, 45], [2021, 320, 48], [2022, 335, 50], [2023, 350, 53], [2024, 370, 60]])

fig=plt.figure(figsize=(8, 6), dpi=80)
ax = fig.add_subplot(111)
ax.plot(data[:,0], data[:,1], linewidth=4, color='b', label='Average Home Price')
ax.plot(data[:,0], data[:,2], linewidth=4, color='g', label='Average Rental Price')
ax.set_title("Average Home and Rental Price in the US from 2020 to 2024")
ax.set_xlabel("Year")
ax.set_ylabel("Price (thousands of dollars)")
ax.set_xticks(data[:,0])
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/309.png')
plt.clf()