
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
x = np.arange(2020, 2024, 1)
y1 = np.array([100,150,200,250])
y2 = np.array([40,45,50,55])
y3 = np.array([25,30,35,40])
plt.xticks(x, x, rotation=0)
plt.title("Employee growth and salary changes in a company from 2020 to 2023")
plt.plot(x, y1, label="Number of employees")
plt.plot(x, y2, label="Average salary (thousand dollars)")
plt.plot(x, y3, label="Average hiring rate", color='black')
plt.ylabel('Data')
plt.xlabel('Year')
for a, b in zip(x, y1):
    plt.text(a, b, b, ha='left', va='bottom', fontsize=8)
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='left', va='bottom', fontsize=8)
for a, b in zip(x, y3):
    plt.text(a, b, b, ha='left', va='bottom', fontsize=8)
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.tight_layout()
plt.savefig("line_232.png")
plt.clf()