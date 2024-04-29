
import matplotlib.pyplot as plt
import numpy as np

age = np.array(['18-25', '26-35', '36-45', '46-55', '56-65'])
bmi = np.array([21.5, 22.5, 23.5, 24.5, 25.5])
weight = np.array([150, 175, 200, 225, 250])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(age, bmi, label="Average BMI", color='tab:blue', marker='o')
ax.plot(age, weight, label="Average Weight(lbs)", color='tab:orange', marker='o')

ax.set_xlabel('Age Group', fontsize=12)
ax.set_ylabel('Values', fontsize=12)
ax.set_title('Average BMI and Weight of Adults in the US by Age Group', fontsize=14)

ax.grid(linestyle='--')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

for i,j in zip(age, bmi):
    ax.annotate(str(j), xy=(i,j+0.2))
for i,j in zip(age, weight):
    ax.annotate(str(j), xy=(i,j+5))

plt.xticks(age, age, rotation=45)
fig.tight_layout()

plt.savefig('line chart/png/492.png')
plt.clf()