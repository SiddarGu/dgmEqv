
import matplotlib.pyplot as plt

# Set data
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
employees = [30, 35, 40, 45, 50, 55, 60]
avg_salary = [50000, 60000, 80000, 70000, 90000, 100000, 110000]

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Plot data
ax.plot(year, employees, label="Employees (thousands)", color="royalblue", linestyle="--", marker="o", markersize=8)
ax.plot(year, avg_salary, label="Average Salary (dollars)", color="orangered", linestyle="-", marker="s", markersize=8)

# Add background grids
ax.grid(linestyle="dotted", color="lavender", linewidth=2)

# Add title
plt.title("Growth of Employees and Average Salary in a Company from 2010 to 2016", fontsize=14)

# Add labels
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Count", fontsize=12)

# Add x-ticks
plt.xticks(year)

# Add legend
ax.legend(loc="upper left")

# Annotate value of each data point
for i, j in zip(year, employees):
    ax.annotate(str(j), xy=(i, j + 1), fontsize=10)
for i, j in zip(year, avg_salary):
    ax.annotate("$" + str(j), xy=(i, j + 2500), fontsize=10, rotation=45, ha="center", va="bottom")

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig("line chart/png/194.png")

# Clear current image state
plt.clf()