

import matplotlib.pyplot as plt
import numpy as np

data = np.array([[6, 80, 3.0], [7, 85, 3.2], [8, 90, 3.5], [9, 93, 3.7], [10, 94, 3.8], [11, 96, 3.9], [12, 98, 4.0]])

plt.figure(figsize=(10, 5))
plt.plot(data[:, 0], data[:, 1], label="Average Test Score")
plt.plot(data[:, 0], data[:, 2], label="Average GPA")

plt.title("Average academic performance of students from 6th to 12th grade")
plt.xlabel("Grade")
plt.ylabel("Score/GPA")
plt.legend(loc="best")
plt.xticks(data[:, 0])

for x, y1, y2 in data:
    plt.annotate(f"({x}, {y1:.1f})", (x, y1), fontsize=10)
    plt.annotate(f"({x}, {y2:.1f})", (x, y2), fontsize=10)

plt.tight_layout()
plt.savefig("line chart/png/558.png")
plt.clf()