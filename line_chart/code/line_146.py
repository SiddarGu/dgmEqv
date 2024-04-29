
import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(15, 8))

# set data
data = np.array([[2019, 200, 150, 50], [2020, 210, 180, 45], [2021, 220, 160, 67], [2022, 230, 170, 70], [2023, 240, 185, 75]])
year = data[:, 0]
donations_A = data[:, 1]
donations_B = data[:, 2]
donations_C = data[:, 3]

# plotting
plt.plot(year, donations_A, label='Donations A(million dollars)', color='red')
plt.plot(year, donations_B, label='Donations B(million dollars)', color='green')
plt.plot(year, donations_C, label='Donations C(million dollars)', color='blue')

# setting x, y-label and title
plt.xlabel('Year')
plt.ylabel('Total donations received (million dollars)')
plt.title('Total donations received by three charities from 2019 to 2023')

# setting legend
plt.legend(loc='upper left')

# setting x-axis ticks
plt.xticks(year)

# setting grid
plt.grid()

# tight layout
plt.tight_layout()

# save image
plt.savefig('line chart/png/155.png')

# clear current image state
plt.clf()