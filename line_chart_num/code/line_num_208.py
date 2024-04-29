
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))

x = [2020, 2021, 2022, 2023]
y1 = [1000, 1200, 1100, 1400]
y2 = [5, 6, 7, 8]
y3 = [7, 9, 8, 12]

plt.plot(x, y1, color='red', linestyle='-', marker='o', label='Revenue(billion dollars)')
plt.plot(x, y2, color='green', linestyle='--', marker='^', label='Profit Margin(percentage)')
plt.plot(x, y3, color='blue', linestyle='-.', marker='s', label='Growth Rate(percentage)')

for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y3):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

plt.xticks(x)
plt.title('Revenue and Profit Margin of a Business from 2020 to 2023')
plt.xlabel('Year')
plt.ylabel('Values')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/285.png')
plt.clf()