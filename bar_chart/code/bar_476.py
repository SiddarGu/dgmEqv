
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(10, 8))

# Draw a bar chart
ax = plt.subplot()
ax.bar("Accounting", 30, color="b", bottom=0, label="Accounting")
ax.bar("Accounting", 75000, color="g", bottom=30, label="Average Salary")
ax.bar("Marketing", 50, color="b", bottom=0, label="Marketing")
ax.bar("Marketing", 85000, color="g", bottom=50, label="Average Salary")
ax.bar("IT", 40, color="b", bottom=0, label="IT")
ax.bar("IT", 90000, color="g", bottom=40, label="Average Salary")
ax.bar("HR", 25, color="b", bottom=0, label="HR")
ax.bar("HR", 70000, color="g", bottom=25, label="Average Salary")

# Label x-axis
ax.set_xticks(np.arange(0, 4, 1))
ax.set_xticklabels(["Accounting", "Marketing", "IT", "HR"], rotation=90, wrap=True)

# Label y-axis
ax.set_ylabel("Number of Employees/Average Salaries (USD)")

# Set title
ax.set_title("Number of Employees and Average Salaries of Four Departments in 2021")

# Set legend
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

# Draw grid
ax.grid(axis="y", linestyle="--")

# Automatically adjust the picture size
plt.tight_layout()

# Save picture
plt.savefig("bar chart/png/241.png")

plt.clf()