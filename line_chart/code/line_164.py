
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,5))

x_title = np.array(['New York','California','Texas','Florida'])
y1_data = np.array([1, 3, 2, 4])
y2_data = np.array([2, 4, 3, 5])

plt.plot(x_title, y1_data, label='Average House Price(thousand dollars)', color='red', marker='o', linewidth=3)
plt.plot(x_title, y2_data, label='Average Apartment Price(thousand dollars)', color='blue', marker='o', linewidth=3)

plt.xlabel('Area')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Price(thousand dollars)')

plt.title('Average Housing and Apartment Prices in Major US States')

plt.legend(loc='upper left', bbox_to_anchor=(1,1))

plt.tight_layout()

plt.savefig('line chart/png/516.png')

plt.clf()