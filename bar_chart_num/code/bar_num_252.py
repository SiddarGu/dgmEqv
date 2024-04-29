
import matplotlib.pyplot as plt
import numpy as np

Country = np.array(['USA', 'UK', 'Germany', 'France'])
Factory_A = np.array([50, 55, 40, 45])
Factory_B = np.array([60, 65, 50, 55])
Factory_C = np.array([70, 75, 60, 65])

x = np.arange(len(Country))
width = 0.2

fig, ax = plt.subplots(figsize=(15, 8))
ax.bar(x, Factory_A, width, label='Factory A')
ax.bar(x + width, Factory_B, width, label='Factory B')
ax.bar(x + (width * 2), Factory_C, width, label='Factory C')

ax.set_xticks(x + width)
ax.set_xticklabels(Country)
ax.set_title('Number of factories in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend()

for i in range(len(Country)):
    ax.annotate(str(Factory_A[i]), xy=(x[i] - 0.12, Factory_A[i] + 0.02), rotation=0)
    ax.annotate(str(Factory_B[i]), xy=(x[i] + 0.12, Factory_B[i] + 0.02), rotation=0)
    ax.annotate(str(Factory_C[i]), xy=(x[i] + 0.36, Factory_C[i] + 0.02), rotation=0)

plt.tight_layout()
plt.savefig('Bar Chart/png/45.png')
plt.clf()