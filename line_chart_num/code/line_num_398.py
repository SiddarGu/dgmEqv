
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(14, 8))
ax=plt.subplot()

age=[18,26,36,46,56,66]
num=[500,300,200,100,50,20]

plt.plot(age,num, color='green', linestyle='--', marker='o', markersize=10, markerfacecolor='blue')
ax.set_xticks(age)
ax.set_xlabel('Age', fontsize=14)
ax.set_ylabel('Number of Participants', fontsize=14)
plt.title('Survey of Participants\' Age in Social Sciences and Humanities Research', fontsize=18)
for a,b in zip(age,num):
    ax.annotate("{}".format(b),xy=(a,b+10), rotation=45, ha='center', fontsize=12)

plt.grid(axis='y')
plt.tight_layout()
plt.savefig('line chart/png/450.png')
plt.clf()