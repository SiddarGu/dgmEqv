
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 8))
plt.title("Number of Tourists and Average Price for Tourism Industry in the US from 2019 to 2023")
x_data = ["2019", "2020", "2021", "2022", "2023"]
num_tourists = [25, 30, 35, 40, 45]
avg_price = [150, 200, 250, 300, 400]
plt.plot(x_data, num_tourists, color='red', label='Number of Tourists (in millions)')
plt.plot(x_data, avg_price, color='green', label='Average Price')
plt.xticks(np.arange(5), x_data, rotation=45)
plt.legend(loc="upper left")
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/513.png')
plt.clf()