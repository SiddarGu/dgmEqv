
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 8))

# plt.subplot(3,1,1)
x = ['Fall 2020', 'Spring 2021', 'Summer 2021', 'Fall 2021', 'Spring 2022', 'Summer 2022', 'Fall 2022']
y = [90, 100, 120, 130, 140, 150, 160]

plt.plot(x, y)
plt.title('College Enrollment Numbers from Fall 2020 to Fall 2022', fontsize=14, fontweight='bold')
plt.xlabel('Semester')
plt.ylabel('Enrollment Number')
plt.xticks(np.arange(len(x)), x, rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig('line chart/png/433.png')
plt.clf()