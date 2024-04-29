
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

# Plot data
year = [2017, 2018, 2019, 2020, 2021, 2022]
ecommerce_sales = [2.3, 3.2, 4.1, 5.6, 6.9, 8.2]
retail_sales = [6.9, 7.3, 7.7, 8.5, 9.2, 10.1]

plt.plot(year, ecommerce_sales, linestyle="-", marker="o", color="b", label="E-commerce Sales")
plt.plot(year, retail_sales, linestyle="-", marker="o", color="r", label="Retail Sales")

# Set xticks to prevent interpolation
plt.xticks(year) 

# Configure chart
plt.title("Comparison of E-commerce and Retail Sales in the United States")
plt.xlabel("Year")
plt.ylabel("Sales (billion dollars)")
plt.grid(True, linestyle="--")
plt.legend(loc="best")
plt.tight_layout()

# Save the figure
plt.savefig(r"line chart/png/349.png")
plt.clf()