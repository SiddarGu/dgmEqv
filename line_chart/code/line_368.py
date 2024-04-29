
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2020, 3000, 2500],
                 [2021, 3500, 3000],
                 [2022, 4000, 3500],
                 [2023, 4500, 4000],
                 [2024, 5000, 4500]])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.plot(data[:, 0], data[:, 1], color='blue', label='Revenue')
ax.plot(data[:, 0], data[:, 2], color='red', label='Expenditure')
ax.set_title('Revenue and Expenditure of a Business from 2020 to 2024')
ax.set_xlabel('Year')
ax.set_ylabel('Revenue/Expenditure (million dollars)')
ax.legend(loc='best')
plt.xticks(data[:, 0])
plt.tight_layout()
plt.savefig('line chart/png/139.png')
plt.clf()