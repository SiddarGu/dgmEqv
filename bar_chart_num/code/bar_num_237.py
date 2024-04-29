
import matplotlib.pyplot as plt
import numpy as np

country = ['USA', 'UK', 'Germany', 'France']
Manufacturing_A = [1000, 900, 1100, 800]
Manufacturing_B = [1200, 1300, 1400, 1500]
Manufacturing_C = [800, 1100, 1200, 1400]

x = np.arange(len(country)) 
width = 0.2

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.bar(x-width, Manufacturing_A, width, label='Manufacturing A(million)')
ax.bar(x, Manufacturing_B, width, label='Manufacturing B(million)')
ax.bar(x+width, Manufacturing_C, width, label='Manufacturing C(million)')

ax.set_xticks(x)
ax.set_xticklabels(country)
ax.legend()

plt.title("Manufacturing output in three categories from four countries in 2021")
for i, j in enumerate(Manufacturing_A):
    ax.annotate(str(j), xy=(i-width/2.5, j+50))
for i, j in enumerate(Manufacturing_B):
    ax.annotate(str(j), xy=(i-width/2, j+50))
for i, j in enumerate(Manufacturing_C):
    ax.annotate(str(j), xy=(i+width/2.5, j+50))

plt.tight_layout()
plt.savefig('Bar Chart/png/209.png')
plt.clf()