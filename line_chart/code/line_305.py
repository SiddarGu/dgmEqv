
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot(1,1,1)
ax.set_title('Changes in Home Prices in the US from 2020 to 2024') 
ax.set_ylabel('Price (million dollars)')
ax.set_xlabel('Year')

data = np.array([[2020, 350, 500],
                 [2021, 370, 550],
                 [2022, 400, 600],
                 [2023, 430, 650],
                 [2024, 460, 700]])

x_labels = ['2020', '2021', '2022', '2023', '2024']
ax.plot(data[:, 0], data[:, 1], label="Median Home Price")
ax.plot(data[:, 0], data[:, 2], label="Average Home Price")
ax.legend(loc='upper left', fontsize='large')
ax.set_xticks(data[:, 0])
ax.set_xticklabels(x_labels, rotation=45, ha='right', wrap=True)
plt.tight_layout()

plt.savefig('line chart/png/443.png')
plt.clf()