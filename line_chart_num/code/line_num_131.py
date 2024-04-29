
import matplotlib.pyplot as plt 
import numpy as np 

age = np.array([18,25,35,45,55,65,75])
avg_income = np.array([35000,40000,45000,50000,55000,45000,35000])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)
ax.plot(age,avg_income,color='green',marker="o",label="Average Income")
ax.set_title("Average Income by Age Group in the United States in 2020")
ax.legend(loc="best")
ax.set_xticks(age)
ax.set_xlabel("Age")
ax.set_ylabel("Average Income (dollars)")

for i,j in zip(age,avg_income):
    ax.annotate(str(j),xy=(i,j))
plt.tight_layout()
plt.savefig("line chart/png/491.png")
plt.clf()