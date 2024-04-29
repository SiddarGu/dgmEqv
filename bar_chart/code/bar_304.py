
import matplotlib.pyplot as plt 
import numpy as np

city = ["New York", "Los Angeles", "Chicago", "Houston"]
number_of_houses_sold = [200, 250, 150, 300]
average_price = [400000, 450000, 350000, 320000]

plt.figure(figsize=(10,5))
ax = plt.subplot()
ax.bar(city, number_of_houses_sold, color="green", label="Number of Houses Sold")
ax.bar(city, average_price, color="red", bottom=number_of_houses_sold, label="Average Price")
plt.xticks(np.arange(len(city)), city, rotation=90)
plt.ylabel("Number & Price")
plt.xlabel("Cities")
plt.title("Number of houses sold and average price in four major cities in 2021")
plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig("bar chart/png/287.png")
plt.clf()